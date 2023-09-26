def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")

    def say_less_than_20(n):
        words = [
            "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        ]
        return words[n]

    def say_tens(n):
        words = [
            "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
        ]
        return words[n - 2]

    def say_hundreds(n):
        return f"{say_less_than_20(n)} hundred"

    def say_thousands(n):
        return f"{say_less_than_20(n)} thousand"

    def say_millions(n):
        return f"{say_less_than_20(n)} million"

    def say_billions(n):
        return f"{say_less_than_20(n)} billion"

    def say_chunks(n):
        if n < 20:
            return say_less_than_20(n)
        elif n < 100:
            return f"{say_tens(n // 10)}-{say_less_than_20(n % 10)}"
        elif n < 1_000:
            return f"{say_hundreds(n // 100)} {say_chunks(n % 100)}"
        elif n < 1_000_000:
            return f"{say_chunks(n // 1_000)} thousand {say_chunks(n % 1_000)}"
        elif n < 1_000_000_000:
            return f"{say_chunks(n // 1_000_000)} million {say_chunks(n % 1_000_000)}"
        else:
            return f"{say_chunks(n // 1_000_000_000)} billion {say_chunks(n % 1_000_000_000)}"

    return say_chunks(number)
