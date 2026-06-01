class DKPatterns:
    def __init__(self):
        self.patterns = {
            "CPR": r"\b(?:0[1-9]|[12][0-9]|3[01])(?:0[1-9]|1[0-2])[0-9]{2}-[0-9]{4}\b",
            "PASSPORT": r"\b[A-Z][0-9]{8}\b",
            "IBAN": r"\bDK[0-9]{2}[0-9]{4}[0-9]{10}\b",
            "PHONE": r"\b(?:\+45)?[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}[\s.-]?[0-9]{2}\b",
            "CVR": r"\b[0-9]{8}\b",
            "SE_NUMBER": r"\bDK[0-9]{8}\b",
        }

    def get_patterns(self):
        return self.patterns
