def translate(text):
    def translate_word(word):
        vowels = "aeiou"
        vowel_sounds = ("xr", "yt")
        if word.startswith(vowel_sounds) or word[0] in vowels:
            return word + "ay"
        elif "qu" in word:
            qu_index = word.find("qu")
            return word[qu_index+2:] + word[:qu_index+2] + "ay"
        else:
            for i in range(len(word)):
                if word[i] in vowels or (word[i] == "y" and i != 0):
                    return word[i:] + word[:i] + "ay"
            return word  # Fallback for words without vowels or "y"

    return ' '.join(translate_word(word) for word in text.split())
