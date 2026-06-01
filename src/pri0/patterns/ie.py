class IEPatterns:
    def __init__(self):
        self.patterns = {
            "IE_PPS": r"\b[0-9]{7}[A-Z]{1,2}\b",
            "IE_PASSPORT": r"\b[A-Z]{2}[0-9]{7}\b",
            "IE_IBAN": r"\bIE[0-9]{2}[A-Z]{4}[0-9]{14}\b",
            "IE_PHONE": r"\b(?:\+353|0)[1-9][0-9]{1,2}[\s.-]?[0-9]{3,4}[\s.-]?[0-9]{4}\b",
            "IE_VAT": r"\bIE[0-9]{7}[A-Z]{1,2}\b",
            "IE_CRO": r"\b[0-9]{6}\b",
        }

    def get_patterns(self):
        return self.patterns
