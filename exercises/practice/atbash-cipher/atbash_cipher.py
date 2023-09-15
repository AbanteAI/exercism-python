def encode(plain_text):
    pass


def decode(ciphered_text):
    pass

def generate_substitution_dict():
    plain = 'abcdefghijklmnopqrstuvwxyz'
    cipher = plain[::-1]
    substitution_dict = {plain[i]: cipher[i] for i in range(len(plain))}
    return substitution_dict

def atbash(text, substitution_dict):
    result = ''
    for char in text:
        if char.isalpha():
            result += substitution_dict[char.lower()]
        elif char.isnumeric():
            result += char
    return result

def encode(plain_text):
    substitution_dict = generate_substitution_dict()
    encoded_text = atbash(plain_text, substitution_dict)
    return ' '.join([encoded_text[i:i+5] for i in range(0, len(encoded_text), 5)])

def decode(ciphered_text):
    substitution_dict = generate_substitution_dict()
    reversed_dict = {v: k for k, v in substitution_dict.items()}
    return atbash(ciphered_text.replace(' ', ''), reversed_dict)