def trinary(string):
    if not all(c in '012' for c in string):
        return 0
    
    decimal = 0
    power = len(string) - 1
    for digit in string:
        decimal += int(digit) * (3 ** power)
        power -= 1
    
    return decimal
