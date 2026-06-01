class CHPatterns:
    def __init__(self):
        self.patterns = {
            "AHV": r"\b756\.[0-9]{4}\.[0-9]{4}\.[0-9]{2}\b",
            "PASSPORT": r"\b[A-Z][0-9]{7}\b",
            "IBAN": r"\bCH[0-9]{2}[0-9]{5}[0-9]{12}\b",
            "PHONE": r"\b(?:\+41|0)[1-9][0-9][\s.-]?[0-9]{3}[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}\b",
            "UID": r"\bCHE-[0-9]{3}\.[0-9]{3}\.[0-9]{3}\b",
            "VAT": r"\bCHE-[0-9]{3}\.[0-9]{3}\.[0-9]{3}(?:\sMWST|\sTVA|\sIVA)\b",
        }

    def get_patterns(self):
        return self.patterns
