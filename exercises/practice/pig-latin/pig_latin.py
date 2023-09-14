def translate(text):
    pass
def translate_word(word):
    vowels = "aeiou"
    if word[0] in vowels or word[:2] in ("xr", "yt"):
        return word + "ay"
    elif word[:2] in ("qu",):
        return word[2:] + word[:2] + "ay"
    else:
        consonant_cluster_end = 0
        for i, c in enumerate(word):
            if c in vowels or (c == "y" and i > 0):
                break
            if c == "q" and i < len(word) - 1 and word[i + 1] == "u":
                consonant_cluster_end = i + 1
            else:
                consonant_cluster_end = i
        return word[consonant_cluster_end + 1:] + word[:consonant_cluster_end + 1] + "ay"

def translate(text):
    words = text.split()
    translated_words = [translate_word(word) for word in words]
    return " ".join(translated_words)
