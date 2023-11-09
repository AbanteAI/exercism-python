def recite(start_verse, end_verse):
    animals = [
        ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
        ("spider", "It wriggled and jiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird!"),
        ("cat", "Imagine that, to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "She's dead, of course!")
    ]

    def construct_verse(n):
        lines = [f"I know an old lady who swallowed a {animals[n-1][0]}."]
        if n > 1:
            lines.append(animals[n-1][1])
        if n < len(animals):
            for i in range(n-1, 0, -1):
                catch_line = f"She swallowed the {animals[i][0]} to catch the {animals[i-1][0]}"
                if animals[i-1][0] == "spider":
                    catch_line += " that wriggled and jiggled and tickled inside her"
                catch_line += "."
                lines.append(catch_line)
            lines.append(animals[0][1])
        return lines

    verses = []
    for verse_number in range(start_verse, end_verse + 1):
        verses.extend(construct_verse(verse_number) + [""])
    return verses[:-1]  # Remove the last empty string to avoid extra newline at the end