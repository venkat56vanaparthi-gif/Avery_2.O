import json

from app.llm.client import LLMClient
from app.llm.prompts import (
    SYSTEM_PROMPT,
    PLAN_BALANCE_PROMPT
)


class LLMRefiner:

    def __init__(self):

        self.client = LLMClient()

    def refine(
        self,
        question: str,
        service_response: dict
    ) -> str:

        prompt = (
            SYSTEM_PROMPT
            + "\n\n"
            + PLAN_BALANCE_PROMPT.format(
                question=question,
                service_response=json.dumps(
                    service_response,
                    indent=2
                )
            )
        )

        return self.client.invoke(prompt)