class ContextExtractor:

    def extract(self, message: str, params: dict) -> dict:

        message_lower = message.lower()

        context = {
            "message": message,
            "member_id": params.get("member_id"),
            "skill_id": params.get("selected_skill_id"),
            "is_final_response": params.get(
                "isFinalResponse",
                False
            ),
            "needs_llm": params.get(
                "needs_llm",
                True
            ),
            "accumulator": None
        }

        if "medical" in message_lower:
            context["accumulator"] = "medical"

        elif "prescription" in message_lower or "rx" in message_lower:
            context["accumulator"] = "rx"

        elif "dental" in message_lower:
            context["accumulator"] = "dental"

        elif "vision" in message_lower:
            context["accumulator"] = "vision"

        return context