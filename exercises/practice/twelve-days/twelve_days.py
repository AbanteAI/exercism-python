def recite(start_verse, end_verse):
    days = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ]
    gifts = [
        'a Partridge in a Pear Tree.', 'two Turtle Doves,', 'three French Hens,', 'four Calling Birds,', 'five Gold Rings,',
        'six Geese-a-Laying,', 'seven Swans-a-Swimming,', 'eight Maids-a-Milking,', 'nine Ladies Dancing,', 'ten Lords-a-Leaping,',
        'eleven Pipers Piping,', 'twelve Drummers Drumming,'
    ]
    verses = []
    for i in range(start_verse - 1, end_verse):
        verse = f"On the {days[i]} day of Christmas my true love gave to me: "
        if i > 0:
            verse += ', '.join(gifts[i:0:-1]) + ', and ' + gifts[0]
        else:
            verse += gifts[0]
        verses.append(verse)
    return verses