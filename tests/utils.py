from typing import Any, Dict

import heksher.main_client as heksher_main_client
from heksher import AsyncHeksherClient
from heksher.heksher_client import TemporaryClient
from pydantic import BaseModel, Field


class CreateRuleParams(BaseModel):
    setting: str  # The name of the configuration
    feature_values: Dict[str, str]
    value: Any
    metadata: Dict[str, str] = Field(default_factory=dict)


async def declare_settings_inner(heksher_url):
    heksher = AsyncHeksherClient(heksher_url, update_interval=60, context_features=["cid"])
    await heksher.set_as_main()  # we only want to declare settings
    await heksher.close()
    heksher_main_client.Main = TemporaryClient()
