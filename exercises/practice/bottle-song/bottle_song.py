def recite(start, take=1):
    lyrics = [
        "Ten green bottles hanging on the wall,",
        "Ten green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be nine green bottles hanging on the wall.",
        "",
        "Nine green bottles hanging on the wall,",
        "Nine green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be eight green bottles hanging on the wall.",
        "",
        "Eight green bottles hanging on the wall,",
        "Eight green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be seven green bottles hanging on the wall.",
        "",
        "Seven green bottles hanging on the wall,",
        "Seven green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be six green bottles hanging on the wall.",
        "",
        "Six green bottles hanging on the wall,",
        "Six green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be five green bottles hanging on the wall.",
        "",
        "Five green bottles hanging on the wall,",
        "Five green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be four green bottles hanging on the wall.",
        "",
        "Four green bottles hanging on the wall,",
        "Four green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be three green bottles hanging on the wall.",
        "",
        "Three green bottles hanging on the wall,",
        "Three green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be two green bottles hanging on the wall.",
        "",
        "Two green bottles hanging on the wall,",
        "Two green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be one green bottle hanging on the wall.",
        "",
        "One green bottle hanging on the wall,",
        "One green bottle hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be no green bottles hanging on the wall."
    ]

    return [lyrics[i-1] for i in range(start, start-take, -1)]
        " green bottles hanging on the wall,",
        " green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be ",
        " green bottles hanging on the wall."
    ]

    verses = []
    for i in range(start, start - take, -1):
        verse = []
        verse.append(f"{i}{lyrics[0]}")
        verse.append(f"{i}{lyrics[1]}")
        verse.append(lyrics[2])
        if i == 1:
            verse.append(f"{lyrics[3]}no{lyrics[4]}")
        else:
            verse.append(f"{lyrics[3]}{i - 1}{lyrics[4]}")
        verses.append("".join(verse))

    return verses
