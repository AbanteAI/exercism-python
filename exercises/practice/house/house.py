def recite(start_verse, end_verse):
def recite(start_verse, end_verse):
    parts = [
        "the house that Jack built.",
        "the malt that lay in ",
        "the rat that ate ",
        "the cat that killed ",
        "the dog that worried ",
        "the cow with the crumpled horn that tossed ",
        "the maiden all forlorn that milked ",
        "the man all tattered and torn that kissed ",
        "the priest all shaven and shorn that married ",
        "the rooster that crowed in the morn that woke ",
        "the farmer sowing his corn that kept ",
        "the horse and the hound and the horn that belonged to "
    ]
    rhyme = "This is "
    verses = []

    for verse_number in range(start_verse, end_verse + 1):
        verse_parts = parts[:verse_number]
        verse = rhyme + "".join(reversed(verse_parts))
        verses.append(verse.strip())

    return verses