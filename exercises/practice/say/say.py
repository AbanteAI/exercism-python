def say(number):
    if number == 0:
        return "zero"
    elif number == 1:
        return "one"
    elif number == 2:
        return "two"
    # Add cases for numbers from 3 to 99
    elif number == 100:
        return "one hundred"
    # Add cases for numbers from 101 to 999
    elif number == 1000:
        return "one thousand"
    # Add cases for numbers from 1001 to 999,999,999,999
    else:
        raise ValueError("Number out of range")
def break_into_chunks(number):
    # Implement breaking the number into chunks of thousands

    # Implement inserting the appropriate scale word between chunks
    pass
    chunks = []
    while number > 0:
        chunk = number % 1000
        chunks.append(chunk)
        number //= 1000
    return chunks[::-1]


    words = []
    for i, chunk in enumerate(chunks):
        if chunk == 0:
            continue
        words.append(say(chunk))
        if i < len(chunks) - 1:
            scale_word = get_scale_word(len(chunks) - i - 1)
            words.append(insert_scale_word(chunk, scale_word))
    return ' '.join(words)