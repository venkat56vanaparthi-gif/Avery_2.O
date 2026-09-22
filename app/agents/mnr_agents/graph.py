from typing import TypedDict, Optional

from langgraph.graph import StateGraph, START, END

from app.agents.base_agent import BaseAgent
from app.skills.skill_router import SkillRouter
from app.skills.plan_balance.skill import PlanBalanceSkill
from app.llm.refine import LLMRefiner


class MNRState(TypedDict, total=False):

    message: str
    member_id: Optional[str]
    accumulator: Optional[str]

    skill_id: Optional[str]

    service_response: dict

    response: str


class MNRAgent(BaseAgent):

    def __init__(self):

        self.skill_router = SkillRouter()

        self.plan_balance_skill = PlanBalanceSkill()

        self.llm_refiner = LLMRefiner()

        self.graph = self._build_graph()

    def _build_graph(self):

        workflow = StateGraph(MNRState)

        workflow.add_node(
            "route_skill",
            self.route_skill
        )

        workflow.add_node(
            "execute_skill",
            self.execute_skill
        )

        workflow.add_node(
            "refine_response",
            self.refine_response
        )

        workflow.add_edge(
            START,
            "route_skill"
        )

        workflow.add_edge(
            "route_skill",
            "execute_skill"
        )

        workflow.add_edge(
            "execute_skill",
            "refine_response"
        )

        workflow.add_edge(
            "refine_response",
            END
        )

        return workflow.compile()

    def route_skill(self, state: MNRState):

        skill_id = self.skill_router.route(
            state["message"],
            state.get("skill_id")
        )

        return {
            "skill_id": skill_id
        }

    def execute_skill(self, state: MNRState):

        skill_id = state.get("skill_id")

        if skill_id == "plan_balance":

            result = self.plan_balance_skill.execute(
                state
            )

        else:

            result = {
                "status": "unsupported",
                "message": "Requested skill is not available."
            }

        return {
            "service_response": result
        }

    def refine_response(self, state: MNRState):

        response = self.llm_refiner.refine(
            state["message"],
            state["service_response"]
        )

        return {
            "response": response
        }

    async def run(self, context: dict):

        result = self.graph.invoke({
            "message": context["message"],
            "member_id": context.get("member_id"),
            "accumulator": context.get("accumulator"),
            "skill_id": context.get("skill_id")
        })

        return {
            "skill_id": result.get("skill_id"),
            "response": result.get("response"),
            "service_response": result.get(
                "service_response"
            )
        }