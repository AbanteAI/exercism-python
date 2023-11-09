import re

def abbreviate(words):
    # Replace hyphens with spaces to treat them as word separators
    words = words.replace('-', ' ')
    # Remove all characters that are not alphabets or spaces
    words = re.sub(r"[^A-Za-z\s]", '', words)
    # Split the words and take the first letter of each, then uppercase it
    acronym = ''.join(word[0].upper() for word in words.split())
    return acronym
