def is_isogram(string):
    letters = []
    for char in string.lower():
        if char.isalpha() and char not in letters:
            letters.append(char)
        elif char.isalpha() and char in letters:
            return False
    return True
