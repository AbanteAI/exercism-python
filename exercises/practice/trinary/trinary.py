def trinary(string):
    if not all(char in "012" for char in string):
        return 0
    
    decimal = 0
    for i, char in enumerate(string[::-1]):
        decimal += int(char) * (3 ** i)
    
    return decimal
