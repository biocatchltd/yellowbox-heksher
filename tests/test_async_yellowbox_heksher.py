from heksher import Setting
from pytest import mark

from tests.utils import declare_settings_inner
from yellowbox_heksher.heksher_service import HeksherService

atest = mark.asyncio


@atest
async def test_get_setting_names(docker_client):
    async with HeksherService.arun(docker_client, heksher_startup_context_features="user") as heksher_service:
        settings = (
            Setting("test_config", type=int, configurable_features=["user"], default_value=1,
                    metadata={"description": "test"})
        )
        await declare_settings_inner(heksher_service.local_url)
        assert heksher_service.get_setting_names() == ["test_config"]
