def recite(start, take=1):
    pass

def verse(bottles):
    number_map = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten"}
    if bottles == 1:
        return (
            f"{number_map[bottles]} green bottle hanging on the wall,\n"
            f"{number_map[bottles]} green bottle hanging on the wall,\n"
            f"And if one green bottle should accidentally fall,\n"
            f"There'll be no green bottles hanging on the wall.\n"
        )
    return (
        f"{number_map[bottles]} green bottles hanging on the wall,\n"
        f"{number_map[bottles]} green bottles hanging on the wall,\n"
        f"And if one green bottle should accidentally fall,\n"
        f"There'll be {number_map[bottles - 1]} green bottles hanging on the wall.\n"
    )

def recite(start, take=1):
    lyrics = []
    for i in range(start, start - take, -1):
        lyrics.extend(verse(i).split('\n')[:-1])
    return lyrics