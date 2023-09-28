def abbreviate(words):
    acronym = ""
    for word in words.split():
        acronym += word[0].upper()
    return acronym