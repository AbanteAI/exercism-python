def recite(start, take=1):
    def num_to_word(num):
        words = ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        return words[num]

    def verse(num):
        line1 = f"{num_to_word(num).capitalize()} green bottle{'s' if num > 1 else ''} hanging on the wall,"
        line4 = f"There'll be {num_to_word(num - 1)} green bottle{'s' if num - 1 > 1 else '' if num - 1 > 0 else 's'} hanging on the wall."
        return f"{line1}\n{line1}\nAnd if one green bottle should accidentally fall,\n{line4}\n{'' if num == 1 else '\\n'}"
    lyrics = []
    lyrics = []
    lyrics = []
    for i in range(start, start - take, -1):
        lyrics.append(verse(i))
    return lyrics
    return lyrics