import re


class Sanitizer:
    def __init__(self, mode: str = "fast"):
        self.mode = mode
        self.common_patterns = {
            # Identificadores España
            # Email (universal)
            "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b",
            # URL (universal)
            "URL": r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+",
            # IP Address (universal)
            "IP_ADDRESS": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
            # Tarjeta de crédito (igual para todos los países)
            "CREDIT_CARD": r"\b(?:\d[ -]*?){13,16}\b",
        }

    def mask(self, text: str, include: list = None) -> str:
        patterns_to_use = self.all_patterns

        if include:
            patterns_to_use = {
                k: v for k, v in self.all_patterns.items() if k in include
            }
        """
        Enmascara los datos sensibles según el modo configurado.
        """
        result = text

        # Lógica de capa rápida (Regex) - Siempre se ejecuta
        for label, pattern in patterns_to_use.items():
            result = re.sub(pattern, f"[{label}]", result)

        # Lógica de capa inteligente (Futura implementación)
        if self.mode == "smart":
            result = self._apply_ai_masking(result)

        return result

    def _apply_ai_masking(self, text: str) -> str:
        # Aquí es donde meteremos el modelo ligero (spaCy o similar) más adelante
        return text + " (Inteligencia aplicada)"
