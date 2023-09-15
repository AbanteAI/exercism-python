import re
def abbreviate(words):
    words = re.sub(r"[^a-zA-Z']+", " ", words).replace("-", " ")
    words_list = words.split()
    acronym = "".join([word[0].upper() for word in words_list])
    return acronym
