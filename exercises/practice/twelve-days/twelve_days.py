def recite(start_verse, end_verse):
    days = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, "
    ]

    verses = []

    for verse in range(start_verse, end_verse + 1):
        current_verse = f"On the {days[verse - 1]} day of Christmas my true love gave to me: "
        current_gifts = gifts[verse - 1::-1]
        if verse > 1:
            current_gifts[0] = "and " + current_gifts[0]
        current_verse += "".join(current_gifts)
        verses.append(current_verse)

    return verses