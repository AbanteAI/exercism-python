def recite(start, take=1):
    verses = []
    for _ in range(take):
        if start == 0:
            verses.append("No more bottles of beer on the wall, no more bottles of beer.")
            verses.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        elif start == 1:
            verses.append("1 bottle of beer on the wall,
