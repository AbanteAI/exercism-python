def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion", "trillion"]

    def chunk_number(number, chunk_size):
        while number > 0:
            yield number % chunk_size
            number //= chunk_size

def convert_chunk(chunk):
    words = []
    if chunk >= 100:
        words.append(units[chunk // 100])
        words.append("hundred")
        chunk %= 100
    if chunk >= 20:
        words.append(tens[chunk // 10])
        if chunk % 10:
            words[-1] += "-" + units[chunk % 10]
    elif 0 < chunk < 10:
        words.append(units[chunk])
    elif 10 <= chunk < 20:
        words.append(teens[chunk - 10])
    return ' '.join(words)

    def link_chunks(chunks):
        words = []
        for i, chunk in enumerate(chunks):
            if chunk:
                words.append(convert_chunk(chunk) + (' ' + scales[i] if scales[i] else ''))
        return ' '.join(reversed(words))

    chunks = list(chunk_number(number, 1000))
    return link_chunks(chunks).strip() or 'zero'
