def recite(start_verse, end_verse):
    animals = [
        "fly",
        "spider",
        "bird",
        "cat",
        "dog",
        "goat",
        "cow",
        "horse"
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

def verse(animal_index):
    lines = [f"I know an old lady who swallowed a {animals[animal_index]}."]
    if animal_index == len(animals) - 1:
        lines.append(phrases[animal_index])
    else:
        if animal_index > 0:
            lines.append(phrases[animal_index])
        for i in range(animal_index, 0, -1):
            catch_phrase = f"She swallowed the {animals[i]} to catch the {animals[i-1]}"
            if animals[i-1] == "spider":
                if i == 1 or animals[i] != "bird":
                    catch_phrase += " that wriggled and jiggled and tickled inside her"
                else:
                    catch_phrase += " that wriggled and jiggled and tickled inside her"
            lines.append(catch_phrase + ".")
        lines.append(phrases[0])

    return lines

song = []
for i in range(start_verse - 1, end_verse):
    song.extend(verse(i))
    if i < end_verse - 1:
        song.append("")

return song

    return song[:-1]  # Remove the last empty line