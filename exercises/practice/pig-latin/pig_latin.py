def translate(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = text.split()
    pig_latin_words = []
    
    for word in words:
for word in words:
    if word[0].lower() in vowels or word[:2].lower() in ['xr', 'yt']:
        pig_latin_words.append(word + 'ay')
    elif word[:3].lower() == 'squ':
        pig_latin_words.append(word[3:] + word[:3] + 'ay')
    else:
        consonant_cluster = ''
        i = 0
        while i < len(word) and (word[i].lower() not in vowels or (i > 0 and word[i].lower() == 'y')):
            consonant_cluster += word[i]
            i += 1
        pig_latin_words.append(word[i:] + consonant_cluster + 'ay')
    
    return ' '.join(pig_latin_words)