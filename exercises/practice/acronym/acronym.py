def abbreviate(words):
    # Remove all punctuation except hyphens and split the words
    words = ''.join(char if char.isalnum() or char == '-' else ' ' for char in words)
    words_list = words.replace('-', ' ').split()

    # Take the first letter of each word and convert to uppercase
    # Exclude any single quotes (apostrophes) from the words before taking the first letter
    acronym = ''.join(word.replace("'", "")[0].upper() for word in words_list if word)

    return acronym