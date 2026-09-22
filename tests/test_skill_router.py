from app.skills.skill_router import SkillRouter


def test_plan_balance_skill():

    router = SkillRouter()

    skill = router.route(
        "What is my medical balance?"
    )

    assert skill == "plan_balance"