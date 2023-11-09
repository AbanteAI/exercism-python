import re

def abbreviate(words):
def abbreviate(words):
    # Remove all punctuation except hyphens, convert hyphens to spaces, and remove underscores
    words_clean = re.sub(r'[^\w\s-]|_', '', words).replace('-', ' ')
    # Split the words and take the first letter of each word
    acronym = ''.join(word[0] for word in words_clean.split())
    # Convert to uppercase and return the acronym
    return acronym.upper()
