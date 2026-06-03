import re

from pri0.patterns.base import BaseCountryProvider


# Spain (ES) patterns provider
class ESPatterns(BaseCountryProvider):
    code = "ES"

    patterns = {
        "ES_DNI_NIF": r"(?i)(?:\d[^a-zA-Z0-9]*){8}[^a-zA-Z0-9]*[A-Z]",
        "ES_NIE": r"(?i)[A-Z][^a-zA-Z0-9]*(?:\d[^a-zA-Z0-9]*){7}[A-Z]",
        "ES_SSN": r"(?:\d[^a-zA-Z0-9]*){12}",
        "ES_CIF": r"(?i)[ABCDEFGHJKLMNPQRSUVW][^a-zA-Z0-9]*(?:\d[^a-zA-Z0-9]*){7}[^a-zA-Z0-9]*[0-9A-J]",
        "ES_IBAN": r"(?i)ES[^a-zA-Z0-9]*(?:\d[^a-zA-Z0-9]*){22}",
        "ES_CREDIT_CARD": r"(?:\d[^a-zA-Z0-9]*){13,16}",
        "ES_PHONE": r"(?:(?:\+|00)?34)?[^a-zA-Z0-9]*[6789][^a-zA-Z0-9]*(?:\d[^a-zA-Z0-9]*){8}",
        "ES_PASSPORT": r"(?i)[A-Z]{3}[^a-zA-Z0-9]*(?:\d[^a-zA-Z0-9]*){6}",
    }

    def _clean(self, value: str) -> str:
        return re.sub(r"[^a-zA-Z0-9]", "", value).upper()

    def validate_checksum(self, label: str, value: str) -> bool:

        if label == "ES_DNI_NIF":
            return self._validate_dni(value)
        if label == "ES_NIE":
            return self._validate_nie(value)
        if label == "ES_IBAN":
            return self._validate_iban(value)
        if label == "ES_PHONE":
            return self._validate_phone(value)
        if label == "ES_CREDIT_CARD":
            return self._luhn_check(value)
        if label == "ES_CIF":
            return self._validate_cif(value)
        if label == "ES_SSN":
            return self._validate_ssn(value)
        if label == "ES_PASSPORT":
            return self._validate_passport(value)
        return True

    def _validate_dni(self, dni: str) -> bool:
        dni = self._clean(dni)
        if len(dni) != 9:
            return False

        table = "TRWAGMYFPDXBNJZSQVHLCKE"
        num = dni[:-1]
        letter = dni[-1]

        if not num.isdigit():
            return False
        return table[int(num) % 23] == letter

    def _validate_nie(self, nie: str) -> bool:
        nie = self._clean(nie)
        if len(nie) != 9:
            return False

        mapping = {"X": "0", "Y": "1", "Z": "2"}
        first_char = nie[0]
        if first_char not in mapping:
            return False

        dni_equivalent = mapping[first_char] + nie[1:]
        return self._validate_dni(dni_equivalent)

    def _validate_iban(self, iban: str) -> bool:
        iban = self._clean(iban)
        if len(iban) != 24:
            return False

        rearranged = iban[4:] + iban[:4]

        digits = ""
        for char in rearranged:
            if char.isalpha():
                digits += str(ord(char) - 55)
            else:
                digits += char

        return int(digits) % 97 == 1

    def _validate_phone(self, phone: str) -> bool:
        phone = self._clean(phone)
        if len(phone) == 11 and phone.startswith("34"):
            phone = phone[2:]

        return len(phone) == 9 and phone[0] in "6789"

    def _luhn_check(self, card_number: str) -> bool:
        card_number = self._clean(card_number)
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

    def _validate_cif(self, cif: str) -> bool:
        cif = self._clean(cif)
        if len(cif) != 9:
            return False

        first_char = cif[0]
        digits = cif[1:8]
        last_char = cif[8]

        if not digits.isdigit():
            return False

        even_sum = 0
        odd_sum = 0

        for i, d in enumerate(digits):
            val = int(d)
            if (i + 1) % 2 == 0:
                even_sum += val
            else:
                prod = val * 2
                odd_sum += (prod // 10) + (prod % 10)

        total_sum = even_sum + odd_sum
        last_digit_calc = (10 - (total_sum % 10)) % 10

        cif_letters = "JABCDEFGHI"

        organization_requires_letter = "KPQSNW"

        organization_requires_number = "ABEH"

        if first_char in organization_requires_letter:
            return last_char == cif_letters[last_digit_calc]
        elif first_char in organization_requires_number:
            return last_char == str(last_digit_calc)
        else:
            return (
                last_char == str(last_digit_calc)
                or last_char == cif_letters[last_digit_calc]
            )

    def _validate_ssn(self, ssn: str) -> bool:
        ssn = self._clean(ssn)
        return len(ssn) == 12 and ssn.isdigit()

    def _validate_passport(self, passport: str) -> bool:
        passport = self._clean(passport)
        if len(passport) != 9:
            return False

        letters = passport[:3]
        digits = passport[3:]
        return letters.isalpha() and digits.isdigit()

    def get_patterns(self):
        return self.patterns
