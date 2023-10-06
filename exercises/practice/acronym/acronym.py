import re
def abbreviate(words):
    words = re.findall(r"[a-zA-Z']+", words.replace('-', ' '))
    acronym = ''.join(word[0].upper() for word in words)
    return acronym