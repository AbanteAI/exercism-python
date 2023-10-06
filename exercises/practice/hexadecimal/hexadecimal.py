def hexa(hex_string):
    decimal = 0
    power = 0
    hex_string = hex_string[::-1]
    for char in hex_string:
        if char.isdigit():
            decimal += int(char) * (16 ** power)
        elif 'a' <= char.lower() <= 'f':
            decimal += (ord(char.lower()) - ord('a') + 10) * (16 ** power)
        else:
            raise ValueError("Invalid hexadecimal string")
        power += 1
    return decimal
