class PLPatterns:
    def __init__(self):
        self.patterns = {
            "PESEL": r"\b[0-9]{2}(?:0[1-9]|1[0-2]|2[1-9]|3[0-2])[0-9]{2}[0-9]{5}\b",
            "NIP": r"\b[0-9]{3}-[0-9]{3}-[0-9]{2}-[0-9]{2}\b",
            "REGON": r"\b[0-9]{9}(?:[0-9]{5})?\b",
            "PASSPORT": r"\b[A-Z]{2}[0-9]{7}\b",
            "IBAN": r"\bPL[0-9]{2}[0-9]{8}[0-9]{16}\b",
            "PHONE": r"\b(?:\+48|0)[1-9][0-9]{2}[\s.-]?[0-9]{3}[\s.-]?[0-9]{3}\b",
            "KRS": r"\b[0-9]{10}\b",
        }

    def get_patterns(self):
        return self.patterns
