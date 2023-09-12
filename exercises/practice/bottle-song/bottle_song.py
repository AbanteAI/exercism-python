def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        verse = []
        verse.append(f"{i} green bottle{'s' if i > 1 else ''} hanging on the wall,")
        verse.append(f"{i} green bottle{'s' if i > 1 else ''} hanging on the wall,")
        verse.append("And if one green bottle should accidentally fall,")
        if i == 1:
            verse.append("There'll be no green bottles hanging on the wall.")
        else:
            verse.append(f"There'll be {i - 1} green bottle{'s' if i - 1 > 1 else ''} hanging on the wall.")
        verses.extend(verse)
        if i > start - take + 1:
            verses.append("")
    return verses