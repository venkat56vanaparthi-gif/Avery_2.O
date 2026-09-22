from app.agents.mnr_agents.graph import MNRAgent


class AgentFactory:

    def __init__(self):
        self.agents = {
            "MNR": MNRAgent()
        }

    def get_agent(self, context: dict):

        skill_id = context.get("skill_id")

        if skill_id:
            agent_name = "MNR"
        else:
            agent_name = "MNR"

        return self.agents[agent_name]