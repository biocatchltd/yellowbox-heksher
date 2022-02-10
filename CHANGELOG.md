# yellowbox-heksher Changelog
## Next
### Changed
* Modified HeksherService to inherit from SingleContainerService, use the latest Heksher image (0.4.1) and run `alembic 
  upgrade head` in a separate container before starting the service
