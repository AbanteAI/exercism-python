def recite(start, take=1):
def recite(start, take=1):
    lyrics = ""
    for i in range(start, start - take, -1):
        if i > 1:
            lyrics += f"{i} green bottles hanging on the wall,\n"
            lyrics += f"{i} green bottles hanging on the wall,\n"
            lyrics += "And if one green bottle should accidentally fall,\n"
            lyrics += f"There'll be {i-1} green bottles hanging on the wall.\n\n"
        elif i == 1:
            lyrics += "One green bottle hanging on the wall,\n"
            lyrics += "One green bottle hanging on the wall,\n"
            lyrics += "And if one green bottle should accidentally fall,\n"
            lyrics += "There'll be no green bottles hanging on the wall.\n\n"
    return lyrics.strip()
