from hydra.core.config_store import ConfigStore
from pydantic.dataclasses import dataclass

@dataclass
class GCPConfig:
    project_id: str = "cybulde"


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(name="gcp_config_schema", node=GCPConfig)