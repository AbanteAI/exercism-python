def translate(text):
    def is_vowel_sound(word):
        return word.startswith(('a', 'e', 'i', 'o', 'u')) or word.startswith(('xr', 'yt'))

    def translate_word(word):
        if is_vowel_sound(word):
            return word + 'ay'
        else:
            if word[0:2] == 'qu':
                return word[2:] + 'quay'
            for i in range(len(word)):
                if word[i] in 'aeiou' or (word[i] == 'y' and i != 0):
                    if word[i-1:i+1] == 'qu':
                        return word[i+1:] + word[:i+1] + 'ay'
                    else:
                        return word[i:] + word[:i] + 'ay'
            return word + 'ay'  # Fallback for words without vowels

    return ' '.join(translate_word(word) for word in text.split())
