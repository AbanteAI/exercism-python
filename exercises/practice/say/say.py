def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    if number == 0:
        return "zero"

    ones = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    tens = [
        "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    teens = [
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    def say_chunk(chunk):
        if chunk == 0:
            return ""
        elif chunk < 10:
            return ones[chunk - 1]
        elif chunk < 20:
            return teens[chunk - 11]
        else:
            result = tens[chunk // 10 - 1]
            if chunk % 10 != 0:
                result += "-" + ones[chunk % 10 - 1]
            return result

    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000

    scale = [
        "", "thousand", "million", "billion"
    ]
    result = ""
    for i, chunk in enumerate(chunks):
        if chunk != 0:
            result = say_chunk(chunk) + " " + scale[i] + " " + result

    return result.strip()
