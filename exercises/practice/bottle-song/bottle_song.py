def recite(start, take=1):
    def bottle_phrase(n):
        if n == 0:
            return "no green bottles"
        elif n == 1:
            return "one green bottle"
        else:
            return f"{n} green bottles"

    lyrics = []
    for i in range(start, start - take, -1):
        verse = []
        verse.append(f"{bottle_phrase(i)} hanging on the wall,")
        verse.append(f"{bottle_phrase(i)} hanging on the wall,")
        verse.append("And if one green bottle should accidentally fall,")
        verse.append(f"There'll be {bottle_phrase(i - 1)} hanging on the wall.")
        lyrics.extend(verse)
        if i > start - take:
            lyrics.append("")

    return lyrics