def recite(start_verse, end_verse):
    animals = [
        "fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"
    ]
    phrases = [
        "I don't know why she swallowed the fly. Perhaps she'll die.",
        "It wriggled and jiggled and tickled inside her.",
        "How absurd to swallow a bird!",
        "Imagine that, to swallow a cat!",
        "What a hog, to swallow a dog!",
        "Just opened her throat and swallowed a goat!",
        "I don't know how she swallowed a cow!",
        "She's dead, of course!"
    ]
    verses = []

    for i in range(start_verse, end_verse + 1):
        verse_lines = [f"I know an old lady who swallowed a {animals[i-1]}."]
        if i > 1:
            verse_lines.append(phrases[i-1])
        if i < len(animals):
            for j in range(i, 1, -1):
                animal1 = animals[j-1]
                animal2 = animals[j-2]
                if animal1 == "spider" and j > 2:
                    animal1 += " that wriggled and jiggled and tickled inside her"
                verse_lines.append(f"She swallowed the {animal1} to catch the {animal2}.")
            verse_lines.append(phrases[0])
        else:
            verse_lines.append(phrases[-1])
        verses.extend(verse_lines)

    return verses