import math

def cipher_text(plain_text):
    normalized_text = "".join(filter(str.isalnum, plain_text.lower()))
    column_count = math.ceil(math.sqrt(len(normalized_text)))
    row_count = math.ceil(len(normalized_text) / column_count)
    padded_text = normalized_text.ljust(column_count * row_count, " ")
    encoded_text = ""
    for i in range(column_count):
        chunk = padded_text[i::column_count]
        if len(chunk) < row_count:
            chunk += " "
        encoded_text += chunk + " "
    return encoded_text.strip()
    return encoded_text.strip()
