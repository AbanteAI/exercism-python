def roman(number):
    roman_numerals = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    
    roman_str = ""
    
    for numeral, value in roman_numerals.items():
        while number >= value:
            roman_str += numeral
            number -= value
            
    return roman_str