def cipher_text(plain_text):
    normalized_text = ''.join(ch.lower() for ch in plain_text if ch.isalnum())
    text_length = len(normalized_text)
    rows = int(text_length ** 0.5)
    cols = rows + 1 if rows * rows < text_length else rows
    chunks = [normalized_text[i:i+cols] for i in range(0, text_length, cols)]
    encoded_text = ' '.join(chunks)
    return encoded_text
