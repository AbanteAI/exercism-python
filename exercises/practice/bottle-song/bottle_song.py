def recite(start, take=1):
    def bottle_text(number):
        if number == 0:
            return "no green bottles"
        elif number == 1:
            return "one green bottle"
        else:
            return f"{number} green bottles"

    def verse(number):
        current_bottles = bottle_text(number)
        next_bottles = bottle_text(number - 1)
        return (f"{current_bottles.capitalize()} hanging on the wall,\n"
                f"{current_bottles.capitalize()} hanging on the wall,\n"
                "And if one green bottle should accidentally fall,\n"
                f"There'll be {next_bottles} hanging on the wall.\n\n")

    lyrics = []
    for i in range(start, start - take, -1):
        lyrics.append(verse(i))
    return lyrics[:-1] + [lyrics[-1].rstrip()]