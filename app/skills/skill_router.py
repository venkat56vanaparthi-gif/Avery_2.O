class SkillRouter:

    def route(
        self,
        message: str,
        selected_skill_id: str | None = None
    ) -> str:

        if selected_skill_id:
            return selected_skill_id

        message_lower = message.lower()

        plan_keywords = [
            "balance",
            "accumulator",
            "deductible",
            "medical",
            "rx",
            "prescription",
            "dental",
            "vision"
        ]

        if any(
            keyword in message_lower
            for keyword in plan_keywords
        ):
            return "plan_balance"

        return "unknown"