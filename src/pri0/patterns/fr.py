class FRPatterns:
    def __init__(self):
        self.patterns = {
            "INSEE": r"\b[12][0-9]{2}(?:0[1-9]|1[0-2]|20)[0-9]{2}[0-9]{3}[0-9]{3}[0-9]{2}\b",
            "CNI": r"\b[0-9]{12}\b",
            "PASSPORT": r"\b[A-Z]{2}[0-9]{7}\b",
            "IBAN": r"\bFR[0-9]{2}(?:\s?[0-9A-Z]{4}){5}[0-9A-Z]{3}\b",
            "PHONE": r"\b0[1-9](?:[\s.-]?[0-9]{2}){4}\b",
            "SIRET": r"\b[0-9]{3}[\s]?[0-9]{3}[\s]?[0-9]{3}[\s]?[0-9]{5}\b",
            "SIREN": r"\b[0-9]{3}[\s]?[0-9]{3}[\s]?[0-9]{3}\b",
        }

    def get_patterns(self):
        return self.patterns
