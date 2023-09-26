def translate(text):
    words = text.split()
    translated_words = []
    for word in words:
        if word[0] in "aeiou" or word[:2] in ["xr", "yt"] or (len(word) > 1 and word[1] == "y"):
            translated_words.append(word + "ay")
        else:
            prefix = ""
            while word and word[0] not in "aeiou":
                if word[:2] == "qu" or (len(word) > 2 and word[1:3] == "qu"):
                    word = word[2:]
                else:
                    prefix += word[0]
                    word = word[1:]
            translated_words.append(word + prefix + "ay")