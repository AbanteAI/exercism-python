def recite(start_verse, end_verse):
    ordinal_numbers = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]
    gifts = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, and ",
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
    for i in range(start_verse, end_verse + 1):
        gifts_text = ", ".join(gifts[i-1:0:-1])
        if i > 1:
            gifts_text += ", and " + gifts[0]
        else:
            gifts_text = gifts[0]
        verse = f"On the {ordinal_numbers[i - 1]} day of Christmas my true love gave to me: {gifts_text}"
        verses.append(verse)

    return verses