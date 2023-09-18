def translate(text):
    pass
def is_vowel(char):
    return char in "aeiou"

def find_first_vowel(word):
    for i, char in enumerate(word):
        if is_vowel(char) or (i == 1 and char == "y") or (i == 0 and (word[:2] in ("xr", "yt") or char in "xy" and is_vowel(word[1]))):
            return i
    return -1

def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        first_vowel = find_first_vowel(word)
        if first_vowel == 0:
            translated_word = word + "ay"
        elif word[first_vowel - 1:first_vowel + 1] == "qu":
            translated_word = word[first_vowel + 1:] + word[:first_vowel + 1] + "ay"
        elif len(word) == 2 and word[1] == "y":
            translated_word = word[1:] + word[0] + "ay"
        elif first_vowel > 0:
            translated_word = word[first_vowel:] + word[:first_vowel] + "ay"
        else:
            translated_word = word
        translated_words.append(translated_word)

    return " ".join(translated_words)
