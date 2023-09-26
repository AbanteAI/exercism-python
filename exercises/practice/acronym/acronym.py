def abbreviate(words):
    acronym = ""
    acronym = ""
    words = words.replace("-", " ").replace("_", "").split()
    for word in words:
        acronym += word[0].upper()
    return acronym
