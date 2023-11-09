def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        if i == 0:
            break
        bottles = f"{i} green bottle{'s' if i != 1 else ''}"
        next_bottles = f"{i - 1} green bottle{'s' if i - 1 != 1 else ''}" if i - 1 != 0 else "no green bottles"
        verse = (
            f"{bottles} hanging on the wall,\n"
            f"{bottles} hanging on the wall,\n"
            "And if one green bottle should accidentally fall,\n"
            f"There'll be {next_bottles} hanging on the wall.\n"
        )
        verses.append(verse)
        if i - 1 != start - take:
            verses.append("")
    return verses