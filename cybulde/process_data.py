from cybulde.config_schemas.config_schema import Config
from cybulde.utils.config_utils import get_config


@get_config(config_path="../configs", config_name="config")
def process_data(config: Config) -> None:
    print(config)
    github_access_token = acess_secret_version("cybulde", "cybulde-data-github-access-token")
    print(f"{github_access_token}")


if __name__ == "__main__":
    process_data()  # type: ignore
    
