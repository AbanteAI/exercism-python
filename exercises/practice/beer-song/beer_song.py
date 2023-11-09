def recite(start, take=1):
    verses = []
    for _ in range(take):
        if start == 0:
            verses.append("No more bottles of beer on the wall, no more bottles of beer.")
            verses.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        elif start == 1:
            verses.append("1 bottle of beer on the wall, 1 bottle of beer.")
            verses.append("Take it down and pass it around, no more bottles of beer on the wall.")
        elif start == 2:
            verses.append("2 bottles of beer on the wall, 2 bottles of beer.")
            verses.append("Take one down and pass it around, 1 bottle of beer on the wall.")
        else:
            verses.append(f"{start} bottles of beer on the wall, {start} bottles of beer.")
            verses.append(f"Take one down and pass it around, {start - 1} bottles of beer on the wall.")
        
        start -= 1
        if _ < take - 1:
            verses.append("")  # Add a blank line between verses

    return verses
