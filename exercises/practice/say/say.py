def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["thousand", "million", "billion"]

    def chunk(num):
        if num < 100:
            return [num]
        result = []
        while num > 0:
            result.append(num % 1000)
            num //= 1000
        return result

    def spell(num):
        if num < 10:
            return units[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            if num % 10 == 0:
                return tens[num // 10 - 2]
            else:
                return f"{tens[num // 10 - 2]}-{units[num % 10]}"
        elif num < 1000:
            if num % 100 == 0:
                return f"{units[num // 100]} hundred"
            else:
                return f"{units[num // 100]} hundred {spell(num % 100)}"
        else:
            for idx, scale in enumerate(scales):
                if num < 1000**(idx + 2):
                    break
            base = 1000**(idx + 1)
            left = num // base
            right = num % base
            if right == 0:
                return f"{spell(left)} {scale}"
            else:
                return f"{spell(left)} {scale} {spell(right)}"

    chunks = chunk(number)
    result = []
    for i, num in enumerate(reversed(chunks)):
        if num > 0:
            if i > 0:
                result.append(scales[i - 1])
            result.append(spell(num))
        elif not result:
            result.append(units[0])

    return " ".join(reversed(result)) if result else "zero"
    return " ".join(reversed(result)) if result else "zero"