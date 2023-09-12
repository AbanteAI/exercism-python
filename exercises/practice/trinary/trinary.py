def trinary(string):
    if not all(char in "012" for char in string):
        return 0

    return sum(int(char) * 3 ** index for index, char in enumerate(reversed(string)))