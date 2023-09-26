def trinary(string):
    if not all(char in "012" for char in string):
        return 0
    
    decimal_value = 0
    for i, char in enumerate(reversed(string)):
        decimal_value += int(char) * (3 ** i)
    
    return decimal_value
