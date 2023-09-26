def recite(start_verse, end_verse):
    phrases = [
        "the house that Jack built.",
        "the malt that lay in",
        "the rat that ate",
        "the cat that killed",
        "the dog that worried",
        "the cow with the crumpled horn that tossed",
        "the maiden all forlorn that milked",
        "the man all tattered and torn that kissed",
        "the priest all shaven and shorn that married",
        "the rooster that crowed in the morn that woke",
        "the farmer sowing his corn that kept",
        "the horse and the hound and the horn that belonged to"
    ]

    verses = []
    for i in range(start_verse - 1, end_verse):
        verse = "This is "
        for j in range(i, -1, -1):
            if j == i:
                verse += phrases[j]
            else:
                verse += " " + phrases[j]
        verses.append(verse)

    return verses