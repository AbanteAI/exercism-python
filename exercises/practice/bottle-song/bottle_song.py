def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        bottles = f"{i} green bottle{'s' if i != 1 else ''}"
        next_bottles = f"{i - 1} green bottle{'s' if i - 1 != 1 else ''}" if i > 1 else "no more green bottles"
        verses.append(f"{bottles} hanging on the wall,")
        verses.append(f"{bottles} hanging on the wall,")
        verses.append("And if one green bottle should accidentally fall,")
        if i - 1 == 0:
            verses.append(f"There'll be {next_bottles} hanging on the wall.")
        else:
            verses.append(f"There'll be {next_bottles} hanging on the wall,")
        if i > start - take + 1:
            verses.append("")  # Add a blank line between verses
    return verses