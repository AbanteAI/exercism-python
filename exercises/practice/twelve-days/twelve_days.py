def recite(start_verse, end_verse):
    pass

GIFTS = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming"
]

ORDINALS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]

def ordinal(n):
    return ORDINALS[n - 1]

def recite(start_verse, end_verse):
    verses = []
    for i in range(start_verse, end_verse + 1):
        verse = f"On the {ordinal(i)} day of Christmas my true love gave to me: "
        verse += ", ".join(GIFTS[j] for j in range(i - 1, 0, -1))
        if i > 1:
            verse += ", and "
        verse += GIFTS[0] + "."
        verses.append(verse)
    return verses