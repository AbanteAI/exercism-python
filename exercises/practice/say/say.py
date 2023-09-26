def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    def spell_out(n):
        if n < 20:
            return ones[n]
        elif n < 100:
            return tens[n // 10] + "-" + ones[n % 10] if n % 10 != 0 else tens[n // 10]
        elif n < 1000:
            return ones[n // 100] + " hundred " + spell_out(n % 100) if n % 100 != 0 else ones[n // 100] + " hundred"
        else:
            for i, word in enumerate(["thousand", "million", "billion", "trillion"], 1):
                if n < 1000 ** (i + 1):
                    return spell_out(n // (1000 ** i)) + " " + word + " " + spell_out(n % (1000 ** i))
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    ones = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    def spell_out(n):
        if n < 20:
            return ones[n]
        elif n < 100:
            return tens[n // 10] + "-" + ones[n % 10] if n % 10 != 0 else tens[n // 10]
        elif n < 1000:
            return ones[n // 100] + " hundred " + spell_out(n % 100) if n % 100 != 0 else ones[n // 100] + " hundred"
        else:
            for i, word in enumerate(["thousand", "million", "billion", "trillion"], 1):
                if n < 1000 ** (i + 1):
                    return spell_out(n // (1000 ** i)) + " " + word + " " + spell_out(n % (1000 ** i))

    return spell_out(number)
