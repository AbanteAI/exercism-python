def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

def chunk_to_words(chunk):
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if chunk < 10:
        return units[chunk]
    elif 10 < chunk < 20:
        return teens[chunk - 10]
    elif chunk >= 20 and chunk < 100:
        return tens[chunk // 10] + ('' if chunk % 10 == 0 else '-' + units[chunk % 10])
    elif chunk >= 100:
        return units[chunk // 100] + " hundred" + ('' if chunk % 100 == 0 else ' ' + chunk_to_words(chunk % 100))

def break_into_chunks(number):
    chunks = []
    while number > 0:
        chunks.insert(0, number % 1000)
        number //= 1000
    return chunks

def insert_scale_words(chunks):
    scales = ["", "thousand", "million", "billion"]
    words = []
    for i in range(len(chunks)):
        if chunks[i] != 0:
            words.append(chunk_to_words(chunks[i]) + (' ' + scales[len(chunks) - i - 1] if scales[len(chunks) - i - 1] else ''))
    return words

# Combine chunks into plain English words
words = ' '.join(insert_scale_words(break_into_chunks(number)))
return words.strip()