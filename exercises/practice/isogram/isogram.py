def is_isogram(string):
    if not string:
        return True
    string = string.lower()
    letters = [char for char in string if char.isalpha()]
    return len(letters) == len(set(letters))
