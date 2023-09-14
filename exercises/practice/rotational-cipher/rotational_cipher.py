def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    translator = alphabet[key:] + alphabet[:key]
    return text.translate(str.maketrans(alphabet + alphabet.upper(), translator + translator.upper()))