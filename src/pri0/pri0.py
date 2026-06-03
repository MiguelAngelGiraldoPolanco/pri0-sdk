import importlib
import re

from .patterns.base import BaseCountryProvider


class Sanitizer:
    def __init__(self, mode: str = "fast"):
        self.mode = mode

    def mask(
        self,
        text: str,
        countries: list = None,
        include: list = None,
        common: list = None,
    ) -> str:
        result = text
        active_patterns = self._build_active_patterns(countries, include, common)

        raw_critical_labels = [
            "COMMON_EMAIL",
            "COMMON_IP_ADDRESS",
            "COMMON_URL",
        ]
        for label in raw_critical_labels:
            if label in active_patterns:
                pattern = active_patterns[label]
                provider = BaseCountryProvider._registry.get("COMMON")

                for match in re.finditer(pattern, result):
                    candidate = match.group(0)
                    candidate_clean = candidate.strip(" ,.!?;:\"'()[]{}<>")

                    if not provider or provider.validate_checksum(
                        label, candidate_clean
                    ):
                        result = result.replace(candidate, f"[{label}]")

                del active_patterns[label]

        for label, pattern in active_patterns.items():
            pos = 0

            while True:
                searchable_text = self._sanitize_for_search(result)

                match = re.search(pattern, searchable_text[pos:])
                if not match:
                    break

                start = match.start() + pos
                end = match.end() + pos

                candidate_real = result[start:end]

                provider_code = (
                    "COMMON" if label.startswith("COMMON_") else label.split("_")[0]
                )
                provider = BaseCountryProvider._registry.get(
                    provider_code
                ) or BaseCountryProvider._registry.get("COMMON")

                if provider and provider.validate_checksum(label, candidate_real):
                    result = result[:start] + f"[{label}]" + result[end:]

                    pos = start + len(f"[{label}]")
                else:
                    pos = end

        if self.mode == "smart":
            result = self._apply_ai_masking(result)

        return result

    def _build_active_patterns(self, countries, include, common):
        active_patterns = {}

        if common:
            if "COMMON" not in BaseCountryProvider._registry:
                try:
                    importlib.import_module(".patterns.common", package="pri0")
                except ImportError:
                    raise ValueError("Common patterns provider not found.")

            provider = BaseCountryProvider._registry.get("COMMON")
            if provider:
                all_common = provider.get_patterns()

                for item in common:
                    key = f"COMMON_{item.upper()}"
                    if key in all_common:
                        active_patterns[key] = all_common[key]

        if countries:
            for code in countries:
                code = code.upper()
                if code not in BaseCountryProvider._registry:
                    try:
                        importlib.import_module(
                            f".patterns.{code.lower()}", package="pri0"
                        )
                    except ImportError:
                        raise ValueError(f"Country '{code}' not found.")
                provider = BaseCountryProvider._registry.get(code)
                if provider:
                    active_patterns.update(provider.get_patterns())

        if include:
            active_patterns = {k: v for k, v in active_patterns.items() if k in include}

        return active_patterns

    def _sanitize_for_search(self, text: str) -> str:
        text = re.sub(r"([a-zA-Z])(?=\d)", r"\1_", text)
        text = re.sub(r"(\d)(?=[a-zA-Z])", r"\1_", text)
        clean = re.sub(r"[^a-zA-Z0-9\s]", "_", text)
        return clean.upper()

    def _apply_ai_masking(self, text: str) -> str:
        return text + " (Inteligencia aplicada)"
