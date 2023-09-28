def recite(start, take=1):
    lyrics = []
    for i in range(take):
        n = start - i
        if n > 2:
            verse = f"{n} bottles of beer on the wall, {n} bottles of beer.\n" \
                    f"Take one down and pass it around, {n - 1} bottles of beer on the wall.\n"
        elif n == 2:
            verse = f"2 bottles of beer on the wall, 2 bottles of beer.\n" \
                    f"Take one down and pass it around, 1 bottle of beer on the wall.\n"
        elif n == 1:
            verse = f"1 bottle of beer on the wall, 1 bottle of beer.\n" \
                    f"Take it down and pass it around, no more bottles of beer on the wall.\n"
        else:
            verse = f"No more bottles of beer on the wall, no more bottles of beer.\n" \
                    f"Go to the store and buy some more, 99 bottles of beer on the wall.\n"
        lyrics.append(verse)
        if i < take - 1:
            lyrics.append("")
    return lyrics