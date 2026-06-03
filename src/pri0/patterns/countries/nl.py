from pri0.patterns.base import BaseCountryProvider


# Netherlands (NL) patterns provider
class NLPatterns(BaseCountryProvider):
    code = "NL"

    def __init__(self):
        self.patterns = {
            "NL_BSN": r"\b[0-9]{9}\b",
            "NL_PASSPORT": r"\b[A-Z]{2}[0-9]{7}\b",
            "NL_IBAN": r"\bNL[0-9]{2}[A-Z]{4}[0-9]{10}\b",
            "NL_PHONE": r"\b(?:\+31|0)[1-9][0-9]{1,3}[\s.-]?[0-9]{3,4}[\s.-]?[0-9]{3,4}\b",
            "NL_BTW": r"\bNL[0-9]{9}B[0-9]{2}\b",
            "NL_KVK": r"\b[0-9]{8}\b",
        }

    def get_patterns(self):
        return self.patterns
