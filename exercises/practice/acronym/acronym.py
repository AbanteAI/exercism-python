import re

def abbreviate(words):
def abbreviate(words):
    # Remove all punctuation including underscores except hyphens
    words = re.sub(r'[^\w\s-]|_', '', words)
    # Replace hyphens with spaces to treat hyphenated words as separate words
    words = words.replace('-', ' ')
    # Split the words and take the first letter of each, then join them as an acronym
    return ''.join(word[0].upper() for word in words.split())
