words = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
    20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}
def say(number):
    pass
def handle_basic_case(number):

    if number < 20:
        return words[number]
    elif number < 100:
        tens, ones = divmod(number, 10)
        return words[tens * 10] + ('-' + words[ones] if ones else '')
def handle_hundreds_case(number):
    hundreds, remainder = divmod(number, 100)
    result = words[hundreds] + " hundred"
    if remainder:
        result += " " + handle_basic_case(remainder)
    return result

def handle_basic_case(number):
    if number < 100:
        return handle_tens_case(number)
    else:
        return handle_hundreds_case(number)

def break_number_into_chunks(number):
    chunks = []
    while number:
        chunks.append(number % 1000)
        number //= 1000
    return chunks[::-1]

def insert_scale_words(chunks):
    scale_words = ["", "thousand", "million", "billion"]
    result = []
    for i, chunk in enumerate(chunks):
        if chunk:
            result.append(f"{handle_basic_case(chunk)} {scale_words[len(chunks) - 1 - i]}")
    return " ".join(result).strip()

def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    chunks = break_number_into_chunks(number)
    return insert_scale_words(chunks)
