# yellowbox-heksher Changelog
## Next
### Changed
* Modified HeksherService to inherit from SingleContainerService 
* Usage of the latest Heksher image (0.4.1) and run `alembic upgrade head` in a separate container before starting Heksher
* Fixed closing of httpx client
