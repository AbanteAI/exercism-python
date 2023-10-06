import re

def abbreviate(words):
    words = re.split(r'[\s-]+', words)
    acronym = ''.join(word[0].upper() for word in words)
    return acronym
