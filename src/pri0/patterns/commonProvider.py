import re

from .base import BaseCountryProvider


class CommonProvider(BaseCountryProvider):
    code = "COMMON"

    patterns = {
        "COMMON_EMAIL": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "COMMON_URL": r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
        "COMMON_IP_ADDRESS": r"\b(?:\d[\s\.]*){4}\b",
        "COMMON_CREDIT_CARD": r"\b(?:\d[\s-]*?){13,16}\b",
    }

    def __init__(self):
        print("DEBUG: CommonProvider ha sido instanciado")
        super().__init__()

    def get_patterns(self):
        return self.patterns

    def validate_checksum(self, label, value):
        print(f"DEBUG: Validando {label} -> Valor original: '{value}'")
        clean_value = value.strip(" ,.!?;:\"'()[]{}<>")

        if label == "COMMON_CREDIT_CARD":
            card_clean = re.sub(r"[\s-]", "", clean_value)
            return self._luhn_check(card_clean)

        if label == "COMMON_IP_ADDRESS":
            ip_clean = re.sub(r"\s+", "", clean_value)
            return self._validate_ip(ip_clean)

        if label == "COMMON_EMAIL":
            return self._validate_email(clean_value)

        if label == "COMMON_URL":
            return self._validate_url(clean_value)

        return True

    def _luhn_check(self, card_number: str) -> bool:
        if not card_number.isdigit():
            return False
        digits = [int(d) for d in card_number]
        checksum = 0
        reverse_digits = digits[::-1]
        for i, digit in enumerate(reverse_digits):
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            checksum += digit
        return checksum % 10 == 0

    def _validate_ip(self, ip: str) -> bool:
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        return all(p.isdigit() and 0 <= int(p) <= 255 for p in parts)

    def _validate_email(self, email: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email.strip()))

    def _validate_url(self, url: str) -> bool:
        pattern = r"^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?$"
        return bool(re.match(pattern, url))
