from .base import BaseCountryProvider


# Belgium (BE) patterns provider
class BEPatterns(BaseCountryProvider):
    code = "BE"

    def __init__(self):
        self.patterns = {
            "BE_RRN": r"\b[0-9]{2}\.[0-9]{2}\.[0-9]{2}-[0-9]{3}\.[0-9]{2}\b",
            "BE_PASSPORT": r"\b[A-Z]{2}[0-9]{6}\b",
            "BE_IBAN": r"\bBE[0-9]{2}[0-9]{3}[0-9]{7}[0-9]{2}\b",
            "BE_PHONE": r"\b(?:\+32|0)[1-9][0-9]{1,2}[\s.-]?[0-9]{2,3}[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}\b",
            "BE_VAT": r"\bBE0[0-9]{9}\b",
            "BE_KBO": r"\b0[0-9]{3}\.[0-9]{3}\.[0-9]{3}\b",
        }

    def get_patterns(self):
        return self.patterns
