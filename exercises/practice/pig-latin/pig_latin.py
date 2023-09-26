def translate(text):
    words = text.split()
    pig_latin_words = []
    for word in words:
        if word[0] in 'aeiou' or word[:2] in ['xr', 'yt']:
            pig_latin_words.append(word + 'ay')
        elif word[:2] == 'qu':
        elif word[:2] in ['qu']:
            pig_latin_words.append(word[2:] + word[:2] + 'ay')
        else:
            for i, c in enumerate(word):
        elif word[0] not in 'aeiouy' or (word[1] == 'y' and word[0] not in 'aeiou'):
                    pig_latin_words.append(word[i:] + word[:i] + 'ay')
                    break
    return ' '.join(pig_latin_words)
