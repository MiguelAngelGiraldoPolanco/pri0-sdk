class DEPatterns:
    def __init__(self):
        self.patterns = {
            # (Sozialversicherungsnummer)
            "DE_SVN": r"\b[0-9]{2}[0-9]{6}[A-Z][0-9]{3}\b",
            "DE_PERSONALAUSWEIS": r"\b[A-Z0-9]{9}\b",
            "DE_PASSPORT": r"\bC[A-Z0-9]{8}\b",
            "DE_IBAN": r"\bDE[0-9]{2}(?:\s?[0-9]{4}){4}[0-9]{2}\b",
            "DE_PHONE": r"\b(?:\+49|0)[1-9][0-9]{1,4}[\s.-]?[0-9]{3,10}\b",
            "DE_STEUER_ID": r"\b[1-9][0-9]{10}\b",
            "DE_UST_ID": r"\bDE[0-9]{9}\b",
            "DE_HANDELSREGISTER": r"\bHR[AB][\s]?[0-9]{4,6}\b",
        }

    def get_patterns(self):
        return self.patterns
