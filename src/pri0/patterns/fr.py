from .base import BaseCountryProvider


# France (FR) patterns provider
class FRPatterns(BaseCountryProvider):
    code = "FR"

    def __init__(self):
        self.patterns = {
            "FR_INSEE": r"\b[12][0-9]{2}(?:0[1-9]|1[0-2]|20)[0-9]{2}[0-9]{3}[0-9]{3}[0-9]{2}\b",
            "FR_CNI": r"\b[0-9]{12}\b",
            "FR_PASSPORT": r"\b[A-Z]{2}[0-9]{7}\b",
            "FR_IBAN": r"\bFR[0-9]{2}(?:\s?[0-9A-Z]{4}){5}[0-9A-Z]{3}\b",
            "FR_PHONE": r"\b0[1-9](?:[\s.-]?[0-9]{2}){4}\b",
            "FR_SIRET": r"\b[0-9]{3}[\s]?[0-9]{3}[\s]?[0-9]{3}[\s]?[0-9]{5}\b",
            "FR_SIREN": r"\b[0-9]{3}[\s]?[0-9]{3}[\s]?[0-9]{3}\b",
        }

    def get_patterns(self):
        return self.patterns
