def recite(start_verse, end_verse):
    verses = []
    for verse_number in range(start_verse, end_verse + 1):
        verse = generate_verse(verse_number)
        verses.append(verse)
    return "\n".join(verses)

def generate_verse(verse_number):
    verses = {
        1: "I know an old lady who swallowed a fly.",
