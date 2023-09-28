def translate(text):
    pass
def find_first_vowel_index(word):
    vowels = "aeiou"
    for index, letter in enumerate(word):
        if index == 0 and letter in ["x", "y"]:
            if word[:2] in ["xr", "yt"]:
                return 0
            else:
                return -1
        if letter in vowels:
            return index
    return -1

def translate(text):
    words = text.split()
for word in words:
    index = find_first_vowel_index(word)
    if index == 0:
        translated_word = word + "ay"
    else:
        if word[index - 1] == "q" and word[index] == "u":
            index += 1
        if word[index - 1] in ["x", "y"] and word[:2] not in ["xr", "yt"]:
            index -= 1
        translated_word = word[index:] + word[:index] + "ay"
    translated_words.append(translated_word)
            if word[index - 1] in ["x", "y"]:
                index -= 1
            translated_word = word[index:] + word[:index] + "ay"
        translated_words.append(translated_word)

    return " ".join(translated_words)
