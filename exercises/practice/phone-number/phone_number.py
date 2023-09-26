class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)
    
    def clean_number(self, number):
        cleaned_number = ""
        for char in number:
            if char.isdigit():
                cleaned_number += char
        if len(cleaned_number) == 11 and cleaned_number[0] == "1":
            cleaned_number = cleaned_number[1:]
        if len(cleaned_number) != 10:
            cleaned_number = "0" * 10
        return cleaned_number
    def clean_number(self, number):
        cleaned_number = ""
        for char in number:
            if char.isdigit():
                cleaned_number += char
        if len(cleaned_number) == 11 and cleaned_number[0] == "1":
            cleaned_number = cleaned_number[1:]
        if len(cleaned_number) != 10:
            cleaned_number = "0" * 10
        return cleaned_number