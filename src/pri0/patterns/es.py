class ESPatterns:
    def __init__(self):
        self.patterns = {
            "ES_DNI_NIF": r"\b[0-9]{8}[A-Z]\b",
            "ES_NIE": r"\b[A-Z][0-9]{7}[A-Z]\b",
            "ES_SSN": r"\b[0-9]{2}[0-9]{8}[0-9]{2}\b",
            "ES_CIF": r"\b[ABCDEFGHJKLMNPQRSUVW][0-9]{7}[0-9A-J]\b",
            "ES_IBAN": r"\b[A-Z]{2}[0-9]{2}(?:\s?[0-9]{4}){4,5}\b",
            "ES_CREDIT_CARD": r"\b(?:\d[ -]*?){13,16}\b",
            "ES_PHONE": r"\b[6789][0-9]{8}\b",
            "ES_EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "ES_URL": r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
            "ES_IP_ADDRESS": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            "ES_PASSPORT": r"\b[A-Z]{3}[0-9]{6}\b",
        }

    def get_patterns(self):
        return self.patterns
