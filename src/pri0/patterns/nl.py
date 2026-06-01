class NLPatterns:
    def __init__(self):
        self.patterns = {
            "BSN": r"\b[0-9]{9}\b",
            "PASSPORT": r"\b[A-Z]{2}[0-9]{7}\b",
            "IBAN": r"\bNL[0-9]{2}[A-Z]{4}[0-9]{10}\b",
            "PHONE": r"\b(?:\+31|0)[1-9][0-9]{1,3}[\s.-]?[0-9]{3,4}[\s.-]?[0-9]{3,4}\b",
            "BTW": r"\bNL[0-9]{9}B[0-9]{2}\b",
            "KVK": r"\b[0-9]{8}\b",
        }

    def get_patterns(self):
        return self.patterns
