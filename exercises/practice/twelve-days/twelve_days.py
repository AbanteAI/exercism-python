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
    for day in range(start_verse, end_verse + 1):
        gifts_list = gifts[:day]
        if day > 1:
            gifts_list[0] = "and " + gifts_list[0]
        verse = f"On the {days[day - 1]} day of Christmas my true love gave to me: " + ", ".join(reversed(gifts_list))
        verses.append(verse)
    
    return verses