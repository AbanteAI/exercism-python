def abbreviate(words):
    words = words.replace("-", " ")
    acronym = ""
        if "_" in word:
            parts = word.split("_")
            for part in parts:
                acronym += part[0].upper()
        else:
            acronym += word[0].upper()
    return acronym
