def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        if i > 2:
            verses.append(f"{i} green bottles hanging on the wall,")
            verses.append(f"{i} green bottles hanging on the wall,")
            verses.append("And if one green bottle should accidentally fall,")
            verses.append(f"There'll be {i - 1} green bottles hanging on the wall.")
        elif i == 2:
            verses.append("Two green bottles hanging on the wall,")
            verses.append("Two green bottles hanging on the wall,")
            verses.append("And if one green bottle should accidentally fall,")
            verses.append("There'll be one green bottle hanging on the wall.")
        else:
            verses.append("One green bottle hanging on the wall,")
            verses.append("One green bottle hanging on the wall,")
            verses.append("And if one green bottle should accidentally fall,")
            verses.append("There'll be no green bottles hanging on the wall.")
        if i != start - take + 1:
            verses.append("")
    return verses