def trinary(string):
    if any(char not in "012" for char in string):
        return 0
    return int(string, 3)