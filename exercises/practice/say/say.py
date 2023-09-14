def say(number):
    pass

def _convert_ones(number):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return ones[number]

def _convert_tens(number):
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    return tens[number]

def _convert_hundreds(number):
    if number == 0:
        return ""
    return _convert_ones(number) + " hundred"

def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number < 10:
        return _convert_ones(number)
    elif number < 100:
        tens, ones = divmod(number, 10)
        if ones:
            return f"{_convert_tens(tens)}-{_convert_ones(ones)}"
        return _convert_tens(tens)
    elif number < 1000:
        hundreds, remainder = divmod(number, 100)
        if remainder:
            return f"{_convert_hundreds(hundreds)} {_convert_tens(remainder)}"
        return _convert_hundreds(hundreds)
    elif number < 1_000_000:
        thousands, remainder = divmod(number, 1000)
        if remainder:
            return f"{say(thousands)} thousand {say(remainder)}"
        return f"{say(thousands)} thousand"
    elif number < 1_000_000_000:
        millions, remainder = divmod(number, 1_000_000)
        if remainder:
            return f"{say(millions)} million {say(remainder)}"
        return f"{say(millions)} million"
    else:
        billions, remainder = divmod(number, 1_000_000_000)
        if remainder:
            return f"{say(billions)} billion {say(remainder)}"
        return f"{say(billions)} billion"