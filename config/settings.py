import os

from dotenv import load_dotenv


load_dotenv()


class Settings:

    GOOGLE_API_KEY = os.getenv(
        "GOOGLE_API_KEY"
    )

    AZURE_OPENAI_API_KEY = os.getenv(
        "AZURE_OPENAI_API_KEY"
    )

    AZURE_OPENAI_ENDPOINT = os.getenv(
        "AZURE_OPENAI_ENDPOINT"
    )

    BENEFITS_SERVICE_URL = os.getenv(
        "BENEFITS_SERVICE_URL"
    )

    PROFILE_SERVICE_URL = os.getenv(
        "PROFILE_SERVICE_URL"
    )


settings = Settings()