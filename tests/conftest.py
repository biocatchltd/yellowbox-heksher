import asyncio
from typing import Sequence

import pytest
from docker import DockerClient
from yellowbox.clients import docker_client as _docker_client

from tests.utils import CreateRuleParams, declare_settings_inner
from yellowbox_heksher.heksher_service import HeksherService


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def docker_client() -> DockerClient:
    with _docker_client() as ret:
        yield ret


@pytest.fixture(scope="module")
def _heksher_service(docker_client):
    with HeksherService.run(docker_client, heksher_startup_context_features="user") as service:
        yield service


@pytest.fixture(scope="function")
async def heksher_service(_heksher_service: HeksherService):
    yield _heksher_service
    await _heksher_service.clear()


@pytest.fixture(scope="function")
def add_rules(heksher_service: HeksherService):
    async def _add_rules(rules: Sequence[CreateRuleParams]):
        await declare_settings_inner(heksher_service.local_url)
        for rule in rules:
            (await heksher_service.http_client.post('/api/v1/rules', content=rule.json())).raise_for_status()
    yield _add_rules


@pytest.fixture(scope="function")
def declare_settings(heksher_service: HeksherService):
    async def _declare_settings():
        await declare_settings_inner(heksher_service.local_url)
    yield _declare_settings
