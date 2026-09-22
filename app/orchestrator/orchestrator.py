from app.orchestrator.context_extractor import ContextExtractor
from app.agents.agent_factory import AgentFactory


class Orchestrator:

    def __init__(self):
        self.context_extractor = ContextExtractor()
        self.agent_factory = AgentFactory()

    async def handle_request(self, request: dict) -> dict:

        request_id = request.get("id")
        params = request.get("params", {})

        user_message = params.get("message", "")

        if not user_message:
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -32602,
                    "message": "Message is required"
                }
            }

        # STEP 4
        context = self.context_extractor.extract(
            user_message,
            params
        )

        # STEP 5
        agent = self.agent_factory.get_agent(context)

        # STEP 6 onwards
        response = await agent.run(context)

        return {
            "jsonrpc": "2.0",
            "id": request_id,
            "result": response
        }