import os

from dotenv import load_dotenv


load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Required environment variable '{name}' is not set."
        )

    return value


API_ID = int(get_required_env("API_ID"))
API_HASH = get_required_env("API_HASH")