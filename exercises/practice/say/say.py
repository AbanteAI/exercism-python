def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    def number_to_words(n):
        ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

        if 1 <= n < 10:
            return ones[n]
        elif 10 <= n < 20:
            return teens[n - 10]
        elif 20 <= n < 100:
            return tens[n // 10] + ("-" + ones[n % 10] if n % 10 != 0 else "")

    def number_to_grouped_words(n):
        if n == 0:
            return "zero"
        group_names = ["", "thousand", "million", "billion"]
        groups = []
        group_index = 0

        while n > 0:
            n, group = divmod(n, 1000)
            if group > 0:
                hundreds, remainder = divmod(group, 100)
                words = []
                if hundreds > 0:
                    words.append(number_to_words(hundreds) + " hundred")
                if remainder > 0:
                    words.append(number_to_words(remainder))
                groups.append(" ".join(words) + " " + group_names[group_index])
            group_index += 1

    return " ".join(reversed(groups)).strip()

    return number_to_grouped_words(number)