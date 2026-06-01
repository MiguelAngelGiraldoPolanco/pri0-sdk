class SEPatterns:
    def __init__(self):
        self.patterns = {
            "PERSONNUMMER": r"\b[0-9]{6}[-+][0-9]{4}\b",
            "SAMORDNINGSNUMMER": r"\b[0-9]{2}(?:0[1-9]|1[0-2])(?:6[1-9]|[7-8][0-9]|9[0-1])[-+][0-9]{4}\b",
            "PASSPORT": r"\b[0-9]{8}\b",
            "IBAN": r"\bSE[0-9]{2}(?:\s?[0-9]{4}){4}[0-9]{4}\b",
            "PHONE": r"\b(?:\+46|0)[1-9][0-9]{1,3}[\s.-]?[0-9]{2,3}[\s.-]?[0-9]{2,3}[\s.-]?[0-9]{2}\b",
            "ORG_NUMBER": r"\b[0-9]{2}[2-9][0-9]{3}-[0-9]{4}\b",
            "VAT": r"\bSE[0-9]{10}01\b",
        }

    def get_patterns(self):
        return self.patterns
