import re

def abbreviate(words):
    words = re.findall(r"[A-Za-z']+", words)
    acronym = ''.join(word[0].upper() for word in words)
    return acronym