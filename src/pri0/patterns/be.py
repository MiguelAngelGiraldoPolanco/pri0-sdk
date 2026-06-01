class BEPatterns:
    def __init__(self):
        self.patterns = {
            "RRN": r"\b[0-9]{2}\.[0-9]{2}\.[0-9]{2}-[0-9]{3}\.[0-9]{2}\b",
            "PASSPORT": r"\b[A-Z]{2}[0-9]{6}\b",
            "IBAN": r"\bBE[0-9]{2}[0-9]{3}[0-9]{7}[0-9]{2}\b",
            "PHONE": r"\b(?:\+32|0)[1-9][0-9]{1,2}[\s.-]?[0-9]{2,3}[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}\b",
            "VAT": r"\bBE0[0-9]{9}\b",
            "KBO": r"\b0[0-9]{3}\.[0-9]{3}\.[0-9]{3}\b",
        }

    def get_patterns(self):
        return self.patterns
