def roman(number):
    if not (0 < number < 4000):
        raise ValueError("Number out of range (must be 1-3999)")

    numeral_map = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    result = []
    for value, numeral in numeral_map:
        while number >= value:
            result.append(numeral)
            number -= value

    return ''.join(result)