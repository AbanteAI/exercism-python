def recite(start, take=1):
    lyrics = []
    for _ in range(take):
        if start == 0:
            lyrics.append("No more bottles of beer on the wall, no more bottles of beer.")
            lyrics.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
            start = 99
        else:
            beer = "bottles" if start != 1 else "bottle"
            lyrics.append(f"{start} {beer} of beer on the wall, {start} {beer} of beer.")
            start -= 1
            next_beer = "bottles" if start != 1 else "bottle"
            action = "Take one down and pass it around" if start > 0 else "Take it down and pass it around"
            remaining = f"{start} {next_beer}" if start > 0 else "no more bottles"
            lyrics.append(f"{action}, {remaining} of beer on the wall.")
        lyrics.append("")

    return lyrics[:-1]