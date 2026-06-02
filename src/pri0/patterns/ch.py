from .base import BaseCountryProvider


# Switzerland (CH) patterns provider
class CHPatterns(BaseCountryProvider):
    code = "CH"

    def __init__(self):
        self.patterns = {
            "CH_AHV": r"\b756\.[0-9]{4}\.[0-9]{4}\.[0-9]{2}\b",
            "CH_PASSPORT": r"\b[A-Z][0-9]{7}\b",
            "CH_IBAN": r"\bCH[0-9]{2}[0-9]{5}[0-9]{12}\b",
            "CH_PHONE": r"\b(?:\+41|0)[1-9][0-9][\s.-]?[0-9]{3}[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}\b",
            "CH_UID": r"\bCHE-[0-9]{3}\.[0-9]{3}\.[0-9]{3}\b",
            "CH_VAT": r"\bCHE-[0-9]{3}\.[0-9]{3}\.[0-9]{3}(?:\sMWST|\sTVA|\sIVA)\b",
        }

    def get_patterns(self):
        return self.patterns
