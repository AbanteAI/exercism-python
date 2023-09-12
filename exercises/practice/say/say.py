def say(number):
    pass
def number_to_words(number):
    if 1 <= number < 20:
        return ONES[number - 1]
    elif 20 <= number < 100:
        tens, remainder = divmod(number, 10)
        return TENS[tens - 2] + ('' if remainder == 0 else '-' + ONES[remainder - 1])
    elif 100 <= number < 1000:
        hundreds, remainder = divmod(number, 100)
        return ONES[hundreds - 1] + ' hundred' + ('' if remainder == 0 else ' ' + number_to_words(remainder))
    elif 1000 <= number < 1000000:
        thousands, remainder = divmod(number, 1000)
        return number_to_words(thousands) + ' thousand' + ('' if remainder == 0 else ' ' + number_to_words(remainder))
    elif 1000000 <= number < 1000000000:
        millions, remainder = divmod(number, 1000000)
        return number_to_words(millions) + ' million' + ('' if remainder == 0 else ' ' + number_to_words(remainder))
    elif 1000000000 <= number < 1000000000000:
        billions, remainder = divmod(number, 1000000000)
        return number_to_words(billions) + ' billion' + ('' if remainder == 0 else ' ' + number_to_words(remainder))

ONES = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen',
]

TENS = [
    'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety',
]

def say(number):
    if number < 0 or number >= 1000000000000:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    return number_to_words(number)
