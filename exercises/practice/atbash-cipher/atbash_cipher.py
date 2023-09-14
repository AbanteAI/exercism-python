def encode(plain_text):
    plain_text = plain_text.lower()
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    encoded = []
    count = 0
    for char in plain_text:
        if char.isalnum():
            index = plain.find(char)
            if index != -1:
                encoded_char = cipher[index]
            else:
                encoded_char = char
            encoded.append(encoded_char)
            count += 1
            if count % 5 == 0:
                encoded.append(" ")
    return "".join(encoded).strip()


def decode(ciphered_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    cipher = "zyxwvutsrqponmlkjihgfedcba"
    decoded = []
    for char in ciphered_text:
        if char.isalnum():
            index = cipher.find(char)
            if index != -1:
                decoded_char = plain[index]
            else:
                decoded_char = char
            decoded.append(decoded_char)
    return "".join(decoded)
