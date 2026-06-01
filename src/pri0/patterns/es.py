class ESPatterns:
    def __init__(self):
        self.patterns = {
            "DNI_NIF": r"\b[0-9]{8}[A-Z]\b",
            "NIE": r"\b[A-Z][0-9]{7}[A-Z]\b",
            "SSN": r"\b[0-9]{2}[0-9]{8}[0-9]{2}\b",
            "CIF": r"\b[ABCDEFGHJKLMNPQRSUVW][0-9]{7}[0-9A-J]\b",
            "IBAN": r"\b[A-Z]{2}[0-9]{2}(?:\s?[0-9]{4}){4,5}\b",
            "CREDIT_CARD": r"\b(?:\d[ -]*?){13,16}\b",
            "PHONE": r"\b[6789][0-9]{8}\b",
            "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "URL": r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
            "IP_ADDRESS": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            "PASSPORT": r"\b[A-Z]{3}[0-9]{6}\b",
        }

    def get_patterns(self):
        return self.patterns
