from pri0.patterns.base import BaseCountryProvider


# Denmark (DK) patterns provider
class DKPatterns(BaseCountryProvider):
    code = "DK"

    def __init__(self):
        self.patterns = {
            "DK_CPR": r"\b(?:0[1-9]|[12][0-9]|3[01])(?:0[1-9]|1[0-2])[0-9]{2}-[0-9]{4}\b",
            "DK_PASSPORT": r"\b[A-Z][0-9]{8}\b",
            "DK_IBAN": r"\bDK[0-9]{2}[0-9]{4}[0-9]{10}\b",
            "DK_PHONE": r"\b(?:\+45)?[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}\b",
            "DK_CVR": r"\b[0-9]{8}\b",
            "DK_SE_NUMBER": r"\bDK[0-9]{8}\b",
        }

    def get_patterns(self):
        return self.patterns
