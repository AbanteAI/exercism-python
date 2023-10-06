def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        if i > 2:
            verse = f"{i} green bottles hanging on the wall,\n{i} green bottles hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be {i-1} green bottles hanging on the wall."
        elif i == 2:
            verse = f"{i} green bottles hanging on the wall,\n{i} green bottles hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be {i-1} green bottle hanging on the wall."
        else:
            verse = f"{i} green bottle hanging on the wall,\n{i} green bottle hanging on the wall,\nAnd if one green bottle should accidentally fall,\nThere'll be no green bottles hanging on the wall."
        verses.append(verse)
    return verses
