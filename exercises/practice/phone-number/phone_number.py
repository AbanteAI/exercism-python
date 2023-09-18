import re
class PhoneNumber:
    def __init__(self, number):
        cleaned_number = re.sub(r"[^0-9]", "", number)
        if len(cleaned_number) == 11 and cleaned_number[0] == "1":
            cleaned_number = cleaned_number[1:]
        if len(cleaned_number) != 10 or not self._is_valid(cleaned_number):
            raise ValueError("Invalid phone number")
        self.cleaned_number = cleaned_number
        self.cleaned_number = cleaned_number
    def __str__(self):
        return self.cleaned_number
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
    def _is_valid(self, number):
        area_code, exchange_code = number[:3], number[3:6]
        return area_code[0] in "23456789" and exchange_code[0] in "23456789"
    @property
    def area_code(self):
        return self.cleaned_number[:3]

    @property
    def number(self):
        return self.cleaned_number
