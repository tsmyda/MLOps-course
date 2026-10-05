import os
import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml


def export_secrets(path: str = "secrets.yaml") -> None:
    secrets = yaml.safe_load(open(path))
    for key, value in secrets.items():
        os.environ[key] = str(value)


def export_envs(environment: str = "dev") -> None:
    env_file = f"config/.env.{environment}"
    load_dotenv(env_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets()
    settings = Settings()
    print(settings.API_KEY)
    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
