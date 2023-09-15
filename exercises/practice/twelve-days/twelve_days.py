def recite(start_verse, end_verse):
    pass

GIFTS = [
    ("first", "a Partridge in a Pear Tree"),
    ("second", "two Turtle Doves"),
    ("third", "three French Hens"),
    ("fourth", "four Calling Birds"),
    ("fifth", "five Gold Rings"),
    ("sixth", "six Geese-a-Laying"),
    ("seventh", "seven Swans-a-Swimming"),
    ("eighth", "eight Maids-a-Milking"),
    ("ninth", "nine Ladies Dancing"),
    ("tenth", "ten Lords-a-Leaping"),
    ("eleventh", "eleven Pipers Piping"),
    ("twelfth", "twelve Drummers Drumming")
]

def generate_verse(day):
    verse = f"On the {GIFTS[day - 1][0]} day of Christmas my true love gave to me: "
    for i in range(day, 0, -1):
        if i == 1 and day != 1:
            verse += "and "
        verse += GIFTS[i - 1][1]
        if i != 1:
            verse += ", "
        else:
            verse += "."
    return verse

def recite(start_verse, end_verse):
    return [generate_verse(day) for day in range(start_verse, end_verse + 1)]