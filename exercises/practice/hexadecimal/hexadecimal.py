def hexa(hex_string):
    if not all(c in "0123456789abcdef" for c in hex_string):
        raise ValueError("Invalid hexadecimal string")
    
    decimal = 0
    for i, char in enumerate(reversed(hex_string)):
        decimal += int(char, 16) * (16 ** i)
    
    return decimal
