import re
from typing import Dict


class BaseCountryProvider:
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        if hasattr(cls, "code"):
            instance = cls()
            instance._validate_self()
            BaseCountryProvider._registry[cls.code.upper()] = instance

    def _validate_self(self):
        for label, pattern in self.get_patterns().items():
            try:
                re.compile(pattern)
            except re.error:
                raise ValueError(
                    f"Invalid pattern syntax in {self.code}: {label} -> {pattern}"
                )

    def validate_checksum(self, label: str, value: str) -> bool:

        raise NotImplementedError(
            f"CRITICAL SECURITY ERROR: The pattern '{label}' has been registered in "
            f"'{self.code}', but has NO validation logic assigned. "
            f"You must implement explicit validation (mathematical or structural) in your module."
        )

    def get_patterns(self) -> Dict[str, str]:
        raise NotImplementedError("Each provider must implement get_patterns")
