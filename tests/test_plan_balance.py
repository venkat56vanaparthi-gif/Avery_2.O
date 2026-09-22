from app.skills.plan_balance.skill import PlanBalanceSkill


def test_missing_accumulator():

    skill = PlanBalanceSkill()

    result = skill.execute({
        "member_id": "MEMBER001",
        "accumulator": None
    })

    assert result["status"] == "clarification_required"