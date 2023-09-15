import re
def translate(text):
    def pig_latin(word):
        # Rule 1: words starting with vowels
        if re.match(r"^(xr|yt|[aeiou])", word):
            return word + "ay"
        # Rule 2: words starting with consonants
        consonant_cluster = re.match(r"^(?:y|[^aeiou])+", word).group(0)
        # Rule 3: words starting with consonants followed by "qu"
        if re.match(r"^[^aeiouy]*qu", word):
            consonant_cluster += "qu"
        # Rule 4: words with "y" after a consonant cluster
        if "y" in consonant_cluster:
            consonant_cluster = consonant_cluster[:-1] if consonant_cluster != "y" else consonant_cluster
        return word[len(consonant_cluster):] + consonant_cluster + "ay"

    words = text.split()
    translated_words = [pig_latin(word) for word in words]
    return " ".join(translated_words)