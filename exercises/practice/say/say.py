def say(number):
    pass
def handle_small_numbers(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 <= number < 10:
        return ones[number]
    elif 10 <= number < 20:
        return teens[number - 10]
        return tens[number // 10] + ('-' + ones[number % 10] if number % 10 != 0 else "")
    else:
        return ones[number // 100] + " hundred" + (handle_small_numbers(number % 100) if number % 100 != 0 else "")

def break_into_chunks(number):
    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000
    return chunks[::-1]

def insert_scale_words(chunks):
    scale_words = ["", "thousand", "million", "billion"]
    result = []
    for i, chunk in enumerate(chunks):
        if chunk != 0:
            result.append(f"{handle_small_numbers(chunk)} {scale_words[len(chunks) - i - 1]}")
    return " ".join(result).strip()

def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("Number out of range")
    elif number == 0:
        return "zero"
    else:
        chunks = break_into_chunks(number)
        return insert_scale_words(chunks)
