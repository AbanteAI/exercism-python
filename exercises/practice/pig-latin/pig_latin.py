def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    pig_latin_words = []
    for word in words:
        if word[0] in vowels or word[:2] in ['xr', 'yt'] or (len(word) == 2 and word[1] == 'y'):
        else:
            consonant_cluster = ''
            i = 0
            while i < len(word) and word[i] not in vowels:
            while i < len(word) and (word[i] not in vowels or (i == 0 and word[i] == 'y')):
    return ' '.join(pig_latin_words)