from app.services.benefit_services import BenefitsService
from app.services.profile_service import ProfileService


class PlanBalanceSkill:

    def __init__(self):

        self.benefits_service = BenefitsService()
        self.profile_service = ProfileService()

    def execute(self, state: dict) -> dict:

        member_id = state.get("member_id")
        accumulator = state.get("accumulator")

        if not member_id:

            return {
                "status": "error",
                "message": "Member ID is required."
            }

        if not accumulator:

            return {
                "status": "clarification_required",
                "message": (
                    "Which accumulator would you like "
                    "to know about: Medical, Rx, Dental, "
                    "or Vision?"
                )
            }

        profile = self.profile_service.get_profile(
            member_id
        )

        balance = self.benefits_service.get_balance(
            member_id,
            accumulator
        )

        return {
            "status": "success",
            "member": profile,
            "accumulator": accumulator,
            "balance": balance
        }