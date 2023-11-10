def say(number):
    if not 0 <= number <= 999999999999:
        raise ValueError("input out of range")

    # Define the basic numbers
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = ["", "thousand", "million", "billion"]

    def say_chunk(chunk):
        words = []
        if chunk >= 100:
            words.append(ones[chunk // 100])
            words.append("hundred")
            chunk %= 100
        if chunk >= 20:
            words.append(tens[chunk // 10])
            if chunk % 10:
                words.append("-" + ones[chunk % 10])
        elif 10 <= chunk < 20:
            words.append(teens[chunk - 10])
        elif 0 < chunk < 10:
            words.append(ones[chunk])
        return ' '.join(words)

    def break_into_chunks(number):
        chunks = []
        while number > 0:
            chunks.append(number % 1000)
            number //= 1000
        return chunks[::-1]

    def combine_chunks_with_scales(chunks):
        words = []
        for i, chunk in enumerate(chunks):
            if chunk:
                words.append(say_chunk(chunk))
                if scales[len(chunks) - i - 1]:
                    words.append(scales[len(chunks) - i - 1])
        return ' '.join(words)

    chunks = break_into_chunks(number)
    return combine_chunks_with_scales(chunks)