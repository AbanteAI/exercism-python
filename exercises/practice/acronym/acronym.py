import re

def abbreviate(words):
    words = re.sub(r"[^\w'-]+|_", ' ', words).replace('-', ' ').split()
    acronym = ''.join([word[0].upper() for word in words if word[0].isalnum()])
    return acronym
