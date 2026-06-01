class GBPatterns:
    def __init__(self):
        self.patterns = {
            "NINO": r"\b[A-CEGHJ-PR-TW-Z][A-CEGHJ-NPR-TW-Z][0-9]{6}[A-D]\b",
            "PASSPORT": r"\b[0-9]{9}\b",
            "IBAN": r"\bGB[0-9]{2}[A-Z]{4}[0-9]{14}\b",
            "PHONE": r"\b(?:\+44|0)[1-9][0-9]{2,4}[\s.-]?[0-9]{3,4}[\s.-]?[0-9]{3,4}\b",
            "UTR": r"\b[0-9]{10}\b",
            "VAT": r"\bGB[0-9]{9}(?:[0-9]{3})?\b",
            "COMPANIES_HOUSE": r"\b(?:[A-Z]{2})?[0-9]{6,8}\b",
            "NHS": r"\b[0-9]{3}[\s]?[0-9]{3}[\s]?[0-9]{4}\b",
            "SORT_CODE": r"\b[0-9]{2}-[0-9]{2}-[0-9]{2}\b",
        }

    def get_patterns(self):
        return self.patterns
