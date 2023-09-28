def spell_out(number):
    ones = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    
    if number < 0 or number > 99:
        raise ValueError("Number out of range")
    
    if number < 20:
        return ones[number]
    else:
        return tens[number // 10] + "-" + ones[number % 10] if number % 10 != 0 else tens[number // 10]

def chunkify(number):
    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000
    return chunks[::-1]

def scale_word(scale):
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    
    if number < 0 or number > 99:
        raise ValueError("Number out of range")
    
    if number < 20:
        return ones[number]
    else:
        return tens[number // 10] + "-" + ones[number % 10] if number % 10 != 0 else tens[number // 10]

def chunkify(number):
    chunks = []
    while number > 0:
        chunks.append(number % 1000)
        number //= 1000
    return chunks[::-1]

def scale_word(scale):
    scales = ["", "thousand", "million", "billion"]
    return scales[scale]

def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("Number out of range")
    
    if number == 0:
        return "zero"
    
    chunks = chunkify(number)
    result = []
    for i, chunk in enumerate(chunks):
        if chunk != 0:
            result.append(spell_out(chunk))
            result.append(scale_word(len(chunks) - i - 1))
    return " ".join(result)