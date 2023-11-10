def recite(start_verse, end_verse):
    days = [
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
    for verse_num in range(start_verse, end_verse + 1):
        verse = f"On the {days[verse_num - 1]} day of Christmas my true love gave to me: "
        gifts_for_day = gifts[verse_num - 1::-1]
        if verse_num > 1:
            gifts_for_day[0] = "and " + gifts_for_day[0]
        verse += ", ".join(gifts_for_day)
        verses.append(verse)
    
    return verses