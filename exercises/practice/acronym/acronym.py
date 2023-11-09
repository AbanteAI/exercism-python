import re

def abbreviate(words):
def abbreviate(words):
    # Split words by whitespace, hyphens, and ignore underscores, remove other punctuation
    word_list = re.split(r'[\s-_]+', re.sub(r'[^\w\s-]', '', words))
    
    # Take the first letter of each word and convert to uppercase
    acronym = ''.join(word[0].upper() for word in word_list if word)
    
    return acronym
