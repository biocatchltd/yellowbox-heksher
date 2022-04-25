# yellowbox-heksher Changelog
## 0.2.0
### Changed
* Usage of the latest Heksher image by default
* `get_rules`, `get_setting_names`, and `clear` are now synchronous
### Added
* added async startup to the service
* `clear_rules`, `clear_settings` methods
### Fixed
* run `alembic upgrade head` in a separate container before starting Heksher
* Fixed closing of httpx client
### Internal
* Modified HeksherService to inherit from SingleContainerService

