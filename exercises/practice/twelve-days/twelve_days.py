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

def generate_verse(day):
    verse = f"On the {ORDINALS[day - 1]} day of Christmas my true love gave to me: "
    for i in range(day - 1, 0, -1):
        verse += f"{GIFTS[i]}, "
    if day > 1:
        verse += "and "
    verse += f"{GIFTS[0]}."
    return verse

def recite(start_verse, end_verse):
    return [generate_verse(day) for day in range(start_verse, end_verse + 1)]