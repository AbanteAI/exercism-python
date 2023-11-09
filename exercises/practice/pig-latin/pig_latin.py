def translate(text):
def translate(text):
    def translate_word(word):
        vowels = "aeiou"
        # Rule 1: Words that start with vowel sounds or "xr" and "yt"
        if word.startswith(("a", "e", "i", "o", "u", "xr", "yt")):
            return word + "ay"
        # Rule 3: Words that start with a consonant sound followed by "qu"
        elif word.startswith("qu"):
            return word[2:] + word[:2] + "ay"
        # Rule 4: Words with "y" after a consonant cluster or as the second letter
        elif "y" in word[1:]:
            y_index = word.index("y")
            # Check if 'y' is after a consonant cluster
            if y_index > 1 or (y_index == 1 and len(word) == 2):
                return word[y_index:] + word[:y_index] + "ay"
        # Rule 2: Words that start with a consonant sound
        # Find the index where the first vowel or 'y' occurs
        for i, char in enumerate(word):
            if char in vowels or char == 'y':
                # Handle special case where 'qu' follows the consonant sound
                if word[i-1:i+1] == "qu":
                    return word[i+1:] + word[:i+1] + "ay"
                else:
                    return word[i:] + word[:i] + "ay"
        # If no vowel or 'y' is found, treat the whole word as a consonant sound
        return word + "ay"

    # Split the text into words and translate each word
    return ' '.join(translate_word(word) for word in text.split())