def say(number):
    if not 0 <= number <= 999999999999:
        raise ValueError("input out of range")

    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion"]

    def chunk_number(n, chunk_size):
        while n > 0:
            yield n % chunk_size
            n //= chunk_size

    def convert_chunk(chunk):
        if chunk < 10:
            return units[chunk]
        elif chunk < 20:
            return teens[chunk - 10]
        elif chunk < 100:
            return tens[chunk // 10] + ("-" + units[chunk % 10] if chunk % 10 != 0 else "")
        else:
            return units[chunk // 100] + " hundred" + (" " + convert_chunk(chunk % 100) if chunk % 100 != 0 else "")

    def convert(number):
        if number == 0:
            return units[0]
        chunks = list(chunk_number(number, 1000))
        parts = []
        for i in range(len(chunks)):
            if chunks[i] != 0:
                parts.append(convert_chunk(chunks[i]) + (" " + scales[i] if scales[i] else ""))
        return ' '.join(filter(None, reversed(parts))).strip()

    return convert(number)
