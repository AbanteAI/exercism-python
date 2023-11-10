def recite(start_verse, end_verse):
def recite(start_verse, end_verse):
    parts = [
        "the horse and the hound and the horn\nthat belonged to ",
        "the farmer sowing his corn\nthat kept ",
        "the rooster that crowed in the morn\nthat woke ",
        "the priest all shaven and shorn\nthat married ",
        "the man all tattered and torn\nthat kissed ",
        "the maiden all forlorn\nthat milked ",
        "the cow with the crumpled horn\nthat tossed ",
        "the dog\nthat worried ",
        "the cat\nthat killed ",
        "the rat\nthat ate ",
        "the malt\nthat lay in ",
        "the house that Jack built."
    ]
    rhyme = []
    for verse_number in range(start_verse, end_verse + 1):
        verse_lines = ["This is " + parts[-1]]
        for part in parts[-verse_number:-1]:
            verse_lines.append(part.strip())
        verse = " ".join(verse_lines)
        rhyme.append(verse)
    return rhyme