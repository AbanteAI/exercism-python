def recite(start, take=1):
    verses = []
    for i in range(start, start - take, -1):
        if i > 2:
            verses.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            verses.append(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
        elif i == 2:
            verses.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            verses.append(f"Take one down and pass it around, {i - 1} bottle of beer on the wall.")
        elif i == 1:
            verses.append(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            verses.append("Take it down and pass it around, no more bottles of beer on the wall.")
        else:
            verses.append("No more bottles of beer on the wall, no more bottles of beer.")
            verses.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        if i != start - take + 1:
            verses.append("")
    return verses
