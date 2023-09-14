def recite(start_verse, end_verse):
    animals = [
        ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
        ("spider", "It wriggled and jiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird!"),
        ("cat", "Imagine that, to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "She's dead, of course!"),
    ]

    verses = []
    for i in range(start_verse - 1, end_verse):
        verses.append(f"I know an old lady who swallowed a {animals[i][0]}.")
        if i > 0:
            verses.append(animals[i][1])
        for j in range(i, 0, -1):
            if j == 1 and i > 1:
                verses.append(f"She swallowed the {animals[j][0]} to catch the {animals[j-1][0]} that {animals[1][1][2:].lower()}")
            elif j > 1:
                verses.append(f"She swallowed the {animals[j][0]} to catch the {animals[j-1][0]}.")
        if i < len(animals) - 1:
            verses.append(animals[0][1])
        if i < end_verse - 1:
            verses.append("")

    return verses