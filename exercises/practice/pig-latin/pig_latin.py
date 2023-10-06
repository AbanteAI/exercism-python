import re

def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        if re.match("^[aeiou]|^(xr|yt)", word):
            word += "ay"
        else:
            consonant_cluster = re.match("^[^aeiou]+(?:qu)?|(?<=^.)y", word).group(0)
            word = word[len(consonant_cluster):] + consonant_cluster + "ay"
        translated_words.append(word)

    return " ".join(translated_words)