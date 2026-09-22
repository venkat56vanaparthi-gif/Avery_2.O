class BenefitsService:

    def get_balance(
        self,
        member_id: str,
        accumulator: str
    ) -> dict:

        # Replace this with the actual Benefits API call.

        mock_data = {
            "medical": {
                "remaining": 1250.00,
                "used": 750.00
            },
            "rx": {
                "remaining": 300.00,
                "used": 200.00
            },
            "dental": {
                "remaining": 500.00,
                "used": 100.00
            },
            "vision": {
                "remaining": 250.00,
                "used": 50.00
            }
        }

        return mock_data.get(
            accumulator,
            {
                "remaining": 0,
                "used": 0
            }
        )