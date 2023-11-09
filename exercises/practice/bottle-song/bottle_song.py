def recite(start, take=1):
    verses = []
    for _ in range(take):
        bottles = f"{start} green bottle{'s' if start != 1 else ''}"
        next_bottles = f"{start - 1} green bottle{'s' if start - 1 != 1 else ''}" if start - 1 else "no more green bottles"
        verse = f"{bottles} hanging on the wall,\n{bottles} hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be {next_bottles} hanging on the wall."
        verses.append(verse)
        if start > 1:
            verses.append("")  # Add a blank line between verses
        start -= 1
    return verses