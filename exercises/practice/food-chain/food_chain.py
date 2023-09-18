def recite(start_verse, end_verse):
    verses = [
        ("fly", "", ""),
        ("spider", "It wriggled and jiggled and tickled inside her.", "She swallowed the spider to catch the fly."),
        ("bird", "How absurd to swallow a bird!", "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her."),
        ("cat", "Imagine that, to swallow a cat!", "She swallowed the cat to catch the bird."),
        ("dog", "What a hog, to swallow a dog!", "She swallowed the dog to catch the cat."),
        ("goat", "Just opened her throat and swallowed a goat!", "She swallowed the goat to catch the dog."),
        ("cow", "I don't know how she swallowed a cow!", "She swallowed the cow to catch the goat."),
        ("horse", "She's dead, of course!", "")
    ]

    lyrics = []
    for verse_number in range(start_verse - 1, end_verse):
        animal, unique_line, swallowed_line = verses[verse_number]
        lyrics.append(f"I know an old lady who swallowed a {animal}.")
        lyrics.append(unique_line)

        if verse_number < len(verses) - 1:
            for swallowed_animal_number in range(verse_number, 0, -1):
                lyrics.append(verses[swallowed_animal_number][2])

            lyrics.append("I don't know why she swallowed the fly. Perhaps she'll die.")
        if verse_number < end_verse - 1 or verse_number == 0:
            lyrics.append("")
    return lyrics