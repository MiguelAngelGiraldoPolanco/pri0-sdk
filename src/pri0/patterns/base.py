class BaseCountryProvider:
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if hasattr(cls, "code"):
            BaseCountryProvider._registry[cls.code.lower()] = cls()

    @property
    def get_patterns(self) -> dict:
        raise NotImplementedError("Each provider must implement get_patterns")
