from heksher import Setting
from pytest import mark

from tests.utils import CreateRuleParams
from yellowbox_heksher.heksher_service import HeksherService

atest = mark.asyncio


def test_sanity(heksher_service):
    pass


@atest
async def test_get_setting_names(heksher_service: HeksherService, declare_settings):
    settings = (
        Setting("test_config", type=int, configurable_features=["user"], default_value=1,
                metadata={"description": "test"})
    )
    await declare_settings()
    assert heksher_service.get_setting_names() == ["test_config"]


@atest
async def test_get_rules(heksher_service: HeksherService, add_rules):
    settings = (
        Setting("test_config", type=int, configurable_features=["user"], default_value=1,
                metadata={"description": "test"}),
        Setting("test_config2", type=int, configurable_features=["user"], default_value=1,
                metadata={"description": "test2"}),
    )
    await add_rules([
        CreateRuleParams(setting="test_config", feature_values={"user": "bar"}, value=2),
        CreateRuleParams(setting="test_config2", feature_values={"user": "foo"}, value=2),
    ])
    assert heksher_service.get_rules() == {'test_config': [{'context_features': [['user', 'bar']],
                                                            'metadata': {}, 'rule_id': 1, 'value': 2}],
                                           'test_config2': [{'context_features': [['user', 'foo']],
                                                             'metadata': {}, 'rule_id': 2, 'value': 2}]}


@atest
async def test_get_specific_settings_rules(heksher_service: HeksherService, add_rules):
    settings = (
        Setting("test_config", type=int, configurable_features=["user"], default_value=1,
                metadata={"description": "test"}),
        Setting("test_config2", type=int, configurable_features=["user"], default_value=1,
                metadata={"description": "test2"}),
    )
    await add_rules([
        CreateRuleParams(setting="test_config", feature_values={"user": "bar"}, value=2),
        CreateRuleParams(setting="test_config2", feature_values={"user": "foo"}, value=2),
    ])
    assert heksher_service.get_rules(("test_config",)) == {'test_config': [{'context_features': [['user', 'bar']],
                                                                            'metadata': {}, 'rule_id': 3,
                                                                            'value': 2}]}


@atest
async def test_clear(heksher_service: HeksherService, add_rules):
    settings = (
        Setting("test_config", type=int, configurable_features=["user"], default_value=1,
                metadata={"description": "test"})
    )
    await add_rules([CreateRuleParams(setting="test_config", feature_values={"user": "john"}, value=2)])
    heksher_service.clear()
    assert not heksher_service.get_rules()
    assert not heksher_service.get_setting_names()
