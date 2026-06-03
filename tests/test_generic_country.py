import re
import sys

from pri0.patterns.base import BaseCountryProvider


def validate_country_patterns(country_code, samples):
    """
    Generic validation utility to verify country patterns and checksum logic.
    """
    # 1. Ensure the country provider is registered
    assert country_code in BaseCountryProvider._registry, (
        f"Country '{country_code}' is not registered."
    )

    provider = BaseCountryProvider._registry[country_code]
    patterns = provider.get_patterns()

    for label, pattern in patterns.items():
        # 2. Ensure we have a sample for every pattern defined in the provider
        assert label in samples, (
            f"Missing sample data for pattern '{label}' in '{country_code}'."
        )

        sample_value = samples[label]
        match = re.search(pattern, sample_value)

        # ==========================================
        print("\n" + "=" * 50, file=sys.stderr)
        print(f"🔍 AUDITING PATTERN: {label}", file=sys.stderr)
        print(f"   - Sample Value: '{sample_value}'", file=sys.stderr)
        print(f"   - Regular Expression: {pattern}", file=sys.stderr)
        if match:
            print(
                f"   - Regex Capture (match.group()): '{match.group()}'",
                file=sys.stderr,
            )
            try:
                checksum_res = provider.validate_checksum(label, match.group())
                print(f"   - Checksum Result: {checksum_res}", file=sys.stderr)
            except Exception as e:
                print(f"   - 💥 CHECKSUM EXCEPTION: {str(e)}", file=sys.stderr)
        else:
            print("   - ❌ REGEX CAPTURED NOTHING (match is None)", file=sys.stderr)
        print("=" * 50 + "\n", file=sys.stderr)
        # ==========================================

        # 3. Verify the regex catches the data structure correctly
        assert match is not None, (
            f"Pattern '{label}' failed to match sample: '{sample_value}'"
        )
        assert match.group() == sample_value, (
            f"Pattern '{label}' matched incorrectly. Expected: '{sample_value}', Got: '{match.group()}'"
        )

        # 4. Verify that the mathematical logic of the Checksum gives the approval
        assert provider.validate_checksum(label, match.group()) is True, (
            f"Pattern '{label}' passed regex but FAILED mathematical checksum validation for value: '{match.group()}'"
        )


# ==============================================================================
# HOW TO USE THIS TEMPLATE:
# 1. Copy this file to your 'tests/' directory (e.g., 'tests/test_es_patterns.py').
# 2. Run 'poetry run pytest tests/test_es_patterns.py' to verify your code.
# ==============================================================================


def test_new_country_validation():
    # --- CONFIGURATION AREA ---
    COUNTRY = "ES"

    # IMPORTANT: This data is mathematically REAL so that it passes the logical validators.
    SAMPLES = {
        "ES_DNI_NIF": "12345@678Z",
        "ES_NIE": "X1234567@L",
        "ES_SSN": "123456.789012",
        "ES_CIF": "A5881.8501",
        "ES_IBAN": "ES13004@9437..67123 10031424",
        "ES_CREDIT_CARD": "5415411@64 4356328",
        "ES_PHONE": "+34612345?678",
        "ES_PASSPORT": "ABC1%23456",
    }
    # --------------------------

    # We force the initialization of the Spanish provider if it hasn't been imported before.

    # (This prevents problems if pytest runs the test in isolation.)
    try:
        import importlib

        importlib.import_module("pri0.patterns.es", package="pri0")
    except ImportError:
        pass

    validate_country_patterns(COUNTRY, SAMPLES)
