def recite(start, take=1):
    verses = []
    verses = []
    for i in range(start, start - take, -1):
        if i > 2:
            verses.append(f"{i} bottles of beer on the wall, {i} bottles of beer.\n"
                          f"Take one down and pass it around, {i - 1} bottles of beer on the wall.\n")
        elif i == 2:
            verses.append("2 bottles of beer on the wall, 2 bottles of beer.\n"
                          "Take one down and pass it around, 1 bottle of beer on the wall.\n")
        elif i == 1:
            verses.append("1 bottle of beer on the wall, 1 bottle of beer.\n"
                          "Take it down and pass it around, no more bottles of beer on the wall.\n")
        else:
            verses.append("No more bottles of beer on the wall, no more bottles of beer.\n"
                          "Go to the store and buy some more, 99 bottles of beer on the wall.\n")
        if i > start - take + 1:
            verses.append("")  # Add a newline between verses except after the last verse.
    return verses
