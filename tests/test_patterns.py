from pri0.pri0 import Sanitizer


def test_all_patterns_are_valid():
    sanitizer = Sanitizer()
    assert sanitizer.validate_patterns() is True


def test_masking_for_all_supported_countries():
    sanitizer = Sanitizer()

    for country_code in sanitizer.providers_patterns.keys():
        text = f"Test with country {country_code}"

        result = sanitizer.mask(text, countries=[country_code])

        assert isinstance(result, str)
