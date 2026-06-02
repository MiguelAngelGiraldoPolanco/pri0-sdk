from .base import BaseCountryProvider


# Portugal (PT) patterns provider
class PTPatterns(BaseCountryProvider):
    code = "PT"

    def __init__(self):
        self.patterns = {
            "PT_NIF": r"\b[123456789][0-9]{8}\b",
            "PT_CC": r"\b[0-9]{8}[A-Z][0-9]{2}\b",
            "PT_PASSPORT": r"\b[A-Z]{2}[0-9]{6}\b",
            "PT_IBAN": r"\bPT[0-9]{2}[0-9]{4}[0-9]{4}[0-9]{11}[0-9]{2}\b",
            "PT_PHONE": r"\b(?:\+351|0)[29][0-9]{2}[\s.-]?[0-9]{3}[\s.-]?[0-9]{3}\b",
            "PT_NIPC": r"\b5[0-9]{8}\b",
            "PT_VAT": r"\bPT[0-9]{9}\b",
        }

    def get_patterns(self):
        return self.patterns
