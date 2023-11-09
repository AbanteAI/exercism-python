def recite(start, take=1):
def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        if i > 2:
            verses.append(f"{i} bottles of beer on the wall, {i} bottles of beer.\n"
                          f"Take one down and pass it around, {i - 1} bottles of beer on the wall.\n")
        elif i == 2:
            verses.append(f"{i} bottles of beer on the wall, {i} bottles of beer.\n"
                          f"Take one down and pass it around, {i - 1} bottle of beer on the wall.\n")
        elif i == 1:
            verses.append(f"{i} bottle of beer on the wall, {i} bottle of beer.\n"
                          f"Take it down and pass it around, no more bottles of beer on the wall.\n")
        else:
            verses.append("No more bottles of beer on the wall, no more bottles of beer.\n"
                          "Go to the store and buy some more, 99 bottles of beer on the wall.\n")
        verses.append("")  # Add an empty line after each verse
    return verses[:-1]  # Remove the last empty line to match the expected output
