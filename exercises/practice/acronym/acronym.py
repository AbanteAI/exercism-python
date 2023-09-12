def abbreviate(words):
    import re
    words = re.split(r'[\s_-]+', words)
    acronym = ''.join(word[0].upper() for word in words)
    return acronym