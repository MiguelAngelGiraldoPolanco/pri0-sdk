import re

from .patterns.registry import country_providers


class Sanitizer:
    def __init__(self, mode: str = "fast"):
        self.mode = mode
        self.providers_patterns = country_providers
        self.common_patterns = {
            "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            "URL": r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
            "IP_ADDRESS": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            "CREDIT_CARD": r"\b(?:\d[ -]*?){13,16}\b",
        }

    def mask(self, text: str, countries: list = None, include: list = None) -> str:

        active_patterns = self.common_patterns.copy()

        if countries:
            for country in countries:
                code = country.lower()
                if code in self.providers_patterns:
                    active_patterns.update(self.providers_patterns[code].get_patterns())

        if include:
            include_upper = [item.upper() for item in include]
            active_patterns = {
                k: v for k, v in active_patterns.items() if k.upper() in include_upper
            }

        result = text
        for label, pattern in active_patterns.items():
            result = re.sub(pattern, f"[{label}]", result)

        if self.mode == "smart":
            result = self._apply_ai_masking(result)

        return result

    def _apply_ai_masking(self, text: str) -> str:
        return text + " (Inteligencia aplicada)"
