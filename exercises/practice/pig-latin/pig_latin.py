import re

def translate(text):
def translate(text):
    def translate_word(word):
        # Rule 1: Words that start with a vowel sound
        if re.match('^[aeiou]|^(xr)|(yt)', word):
            return word + 'ay'
        # Rule 2: Words that start with a consonant sound
        elif re.match('^[^aeiou]+', word):
            # Rule 3: Words that start with a consonant sound followed by "qu"
            consonant_cluster = re.match('^[^aeiou]*qu|^[^aeiou]+', word).group()
            return word[len(consonant_cluster):] + consonant_cluster + 'ay'
        # Rule 4: Words with a "y" after a consonant cluster or as the second letter
        elif re.match('^[^aeiou]?y', word):
            # Handle "y" as the second letter in a two-letter word
            if len(word) == 2 and word[1] == 'y':
                return word[1] + word[0] + 'ay'
            # Handle "y" after a consonant cluster
            else:
                consonant_cluster = re.match('^[^aeiou]+', word).group()
                return word[len(consonant_cluster):] + consonant_cluster + 'ay'
        return word

    return ' '.join(translate_word(word) for word in text.split())

# Note: The implementation assumes that the input text will be a string containing words separated by spaces.
# It does not handle punctuation or capitalization as those cases are not mentioned in the instructions.