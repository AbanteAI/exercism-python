def encode(plain_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse_alphabet = alphabet[::-1]
    ciphered_text = []

    for char in plain_text.lower():
        if char.isalpha():
            index = alphabet.index(char)
            ciphered_text.append(reverse_alphabet[index])
        elif char.isdigit():
            ciphered_text.append(char)

    # Group into 5 characters
    return ' '.join([''.join(ciphered_text[i:i+5]) for i in range(0, len(ciphered_text), 5)])


def decode(ciphered_text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reverse_alphabet = alphabet[::-1]
    decoded_text = []

    for char in ciphered_text.lower():
        if char.isalpha():
            index = reverse_alphabet.index(char)
            decoded_text.append(alphabet[index])
        elif char.isdigit():
            decoded_text.append(char)

    return ''.join(decoded_text)
