class DEPatterns:
    def __init__(self):
        self.patterns = {
            # (Sozialversicherungsnummer)
            "SVN": r"\b[0-9]{2}[0-9]{6}[A-Z][0-9]{3}\b",
            "PERSONALAUSWEIS": r"\b[A-Z0-9]{9}\b",
            "PASSPORT": r"\bC[A-Z0-9]{8}\b",
            "IBAN": r"\bDE[0-9]{2}(?:\s?[0-9]{4}){4}[0-9]{2}\b",
            "PHONE": r"\b(?:\+49|0)[1-9][0-9]{1,4}[\s.-]?[0-9]{3,10}\b",
            "STEUER_ID": r"\b[1-9][0-9]{10}\b",
            "UST_ID": r"\bDE[0-9]{9}\b",
            "HANDELSREGISTER": r"\bHR[AB][\s]?[0-9]{4,6}\b",
        }

    def get_patterns(self):
        return self.patterns
