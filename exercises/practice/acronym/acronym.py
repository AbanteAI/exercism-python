import re

def abbreviate(words):
    words_list = re.findall(r"[a-zA-Z]+'?[a-zA-Z]*", words)
    acronym = ''.join([word[0].upper() for word in words_list])
    return acronym