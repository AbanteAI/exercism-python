def encode(plain_text):
    atbash_table = str.maketrans(
        "abcdefghijklmnopqrstuvwxyz1234567890",
        "zyxwvutsrqponmlkjihgfedcba1234567890",
    )
    plain_text = plain_text.lower().translate(atbash_table)
    return " ".join(plain_text[i:i + 5] for i in range(0, len(plain_text), 5))

def decode(ciphered_text):
    atbash_table = str.maketrans(
        "zyxwvutsrqponmlkjihgfedcba1234567890",
        "abcdefghijklmnopqrstuvwxyz1234567890",
    )
    ciphered_text = ciphered_text.replace(" ", "").translate(atbash_table)
    return ciphered_text