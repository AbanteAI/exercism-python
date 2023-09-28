def recite(start_verse, end_verse):
    animals = [
        ("fly", ""),
        ("spider", "It wriggled and jiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird!"),
        ("cat", "Imagine that, to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "She's dead, of course!")
    ]

    lyrics = []
    for verse in range(start_verse - 1, end_verse):
        lyrics.append(f"I know an old lady who swallowed a {animals[verse][0]}.")
        if verse > 0:
            lyrics.append(animals[verse][1])

        for i in range(verse, 0, -1):
            if i == 1 and verse > 1:
                extra_line = " that wriggled and jiggled and tickled inside her."
            else:
                extra_line = ""

            lyrics.append(f"She swallowed the {animals[i][0]} to catch the {animals[i-1][0]}{extra_line}")

            lyrics.append(f"She swallowed the {animals[i][0]} to catch the {animals[i-1][0]}{extra_line}")


        if verse < 7:
            lyrics.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        lyrics.append("")

    return lyrics