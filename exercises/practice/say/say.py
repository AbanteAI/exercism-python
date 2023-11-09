def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion", "trillion"]

    def chunk_number(number):
        chunks = []
        while number > 0:
            chunks.insert(0, number % 1000)
            number //= 1000
        return chunks

def say_chunk(chunk):
    words = []
    if chunk >= 100:
        words.append(units[chunk // 100])
        words.append("hundred")
        chunk %= 100
    if 20 <= chunk < 100:
        if chunk % 10 == 0:
            words.append(tens[chunk // 10])
        else:
            words.append(tens[chunk // 10] + '-' + units[chunk % 10])
        chunk = 0
    elif 10 <= chunk < 20:
        words.append(teens[chunk - 10])
        chunk = 0
    elif 0 < chunk < 10:
        words.append(units[chunk])
    return ' '.join(words)

def say_number(number):
    if number == 0:
        return units[0]
    chunks = chunk_number(number)
    scale_chunks = [say_chunk(chunk) + (' ' + scales[len(chunks) - index - 1] if chunk else '') for index, chunk in enumerate(chunks)]
    # Join the chunks with appropriate spaces, ensuring that scale words are correctly formatted
    return ' '.join(filter(None, [chunk.strip() for chunk in scale_chunks]))

    return say_number(number).strip()
