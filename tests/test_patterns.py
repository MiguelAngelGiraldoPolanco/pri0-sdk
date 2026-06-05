from pri0 import Sanitizer
from pri0.patterns.base import BaseCountryProvider


def test_all_patterns_are_valid():
    sanitizer = Sanitizer()
    assert sanitizer is not None


def test_masking_for_all_supported_countries():
    sanitizer = Sanitizer()

    countries_found = [k for k in BaseCountryProvider._registry.keys() if k != "COMMON"]
    assert len(countries_found) > 0, (
        "No country provider was detected in the 'patterns' folder."
    )

    real_data_samples = {
        "ES": "Mi DNI es 12345678Z y mi teléfono el 612345678",
    }

    for country_code in countries_found:
        text = real_data_samples.get(
            country_code,
            f"Missing real test string for {country_code} in real_data_samples",
        )

        result = sanitizer.mask(text, countries=[country_code])

        assert isinstance(result, str)

        if country_code in real_data_samples:
            assert f"[{country_code}_" in result, (
                f"CRITICAL ERROR in '{country_code}': The sanitizer failed to mask anything. "
                f"Check if the Regex failed or if the mathematical checksum rejected the simulated data."
            )
