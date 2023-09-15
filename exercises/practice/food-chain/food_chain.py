def recite(start_verse, end_verse):
    verses = [
        ("fly", "I don't know why she swallowed the fly. Perhaps she'll die."),
        ("spider", "It wriggled and jiggled and tickled inside her.", "that wriggled and jiggled and tickled inside her."),
        ("bird", "How absurd to swallow a bird!"),
        ("cat", "Imagine that, to swallow a cat!"),
        ("dog", "What a hog, to swallow a dog!"),
        ("goat", "Just opened her throat and swallowed a goat!"),
        ("cow", "I don't know how she swallowed a cow!"),
        ("horse", "She's dead, of course!")
    ]
    result = []
    for i in range(start_verse - 1, end_verse):
        result.append(f"I know an old lady who swallowed a {verses[i][0]}.")
        result.append(verses[i][1])
        for j in range(i, 0, -1):
            if j == 1 and i != 7:
                result.append(f"She swallowed the {verses[j][0]} to catch the {verses[j-1][0]} {verses[j][2]}")
            elif i != 7:
                result.append(f"She swallowed the {verses[j][0]} to catch the {verses[j-1][0]}.")
        if i != 7:
            result.append(verses[0][1])
        if i != end_verse - 1:
            result.append("")
    return result