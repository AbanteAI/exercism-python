def translate(text):
    words = text.split()
    translated_words = []
    for word in words:
        if word[0] in 'aeiou' or word[:2] in ['xr', 'yt']:
            translated_word = word + 'ay'
        elif word[:2] == 'qu':
            translated_word = word[2:] + word[:2] + 'ay'
        else:
            consonant_cluster = ''
            i = 0
            while i < len(word) and word[i] not in 'aeiou':
            while i < len(word) and (word[i] not in 'aeiou' or (i > 0 and word[i] == 'y')):
            translated_word = word[i:] + consonant_cluster + 'ay'
        translated_words.append(translated_word)
    return ' '.join(translated_words)
