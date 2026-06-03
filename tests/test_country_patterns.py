import re

import pytest

from pri0.patterns.base import BaseCountryProvider

all_countries = BaseCountryProvider._registry.keys()


@pytest.mark.parametrize("country_code", all_countries)
def test_patterns_for_country(country_code):
    provider = BaseCountryProvider._registry[country_code]
    patterns = provider.get_patterns()

    for label, pattern in patterns.items():
        try:
            compiled = re.compile(pattern)
            assert compiled is not None
        except re.error:
            pytest.fail(
                f"The pattern '{label}' for country '{country_code}' is invalid: {pattern}"
            )

    assert len(patterns) > 0, f"Country '{country_code}' has no patterns defined."
