def recite(start, take=1):
def recite(start, take=1):
    verses = [
        "Ten green bottles hanging on the wall,",
        "Ten green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be nine green bottles hanging on the wall.",

        "Nine green bottles hanging on the wall,",
        "Nine green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be eight green bottles hanging on the wall.",

        "Eight green bottles hanging on the wall,",
        "Eight green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be seven green bottles hanging on the wall.",

        "Seven green bottles hanging on the wall,",
        "Seven green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be six green bottles hanging on the wall.",

        "Six green bottles hanging on the wall,",
        "Six green bottles hanging on the wall,",
        "And if one green bottle should accidentally fall,",
        "There'll be five green bottles hanging on the wall.",
    ]

    song = []
    for i in range(start, start - take, -1):
        song.extend(verses[(i - 1) * 4:i * 4])

    return song