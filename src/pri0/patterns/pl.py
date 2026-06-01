class PLPatterns:
    def __init__(self):
        self.patterns = {
            "PL_PESEL": r"\b[0-9]{2}(?:0[1-9]|1[0-2]|2[1-9]|3[0-2])[0-9]{2}[0-9]{5}\b",
            "PL_NIP": r"\b[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}\b",
            "PL_REGON": r"\b[0-9]{9}(?:[0-9]{5})?\b",
            "PL_PASSPORT": r"\b[A-Z]{2}[0-9]{7}\b",
            "PL_IBAN": r"\bPL[0-9]{2}[0-9]{8}[0-9]{16}\b",
            "PL_PHONE": r"\b(?:\+48|0)[1-9][0-9]{2}[\s.-]?[0-9]{3}[\s.-]?[0-9]{3}\b",
            "PL_KRS": r"\b[0-9]{10}\b",
        }

    def get_patterns(self):
        return self.patterns
