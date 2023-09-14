def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        verse = []
        if i > 1:
            verse.append(f"{i} green bottles hanging on the wall,")
            verse.append(f"{i} green bottles hanging on the wall,")
            verse.append("And if one green bottle should accidentally fall,")
            verse.append(f"There'll be {i - 1} green bottles hanging on the wall.")
        elif i == 1:
            verse.append("One green bottle hanging on the wall,")
            verse.append("One green bottle hanging on the wall,")
            verse.append("And if one green bottle should accidentally fall,")
            verse.append("There'll be no green bottles hanging on the wall.")
        if i != start - take + 1:
            verses.append("")
        verses.extend(verse)
    return verses