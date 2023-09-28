import string

def cipher_text(plain_text):
    normalized_text = plain_text.lower().translate(str.maketrans('', '', string.punctuation + ' '))
    num_chars = len(normalized_text)
    num_columns = int(num_chars ** 0.5) + 1
    num_rows = (num_chars + num_columns - 1) // num_columns
    
    rows = [''] * num_rows
    for i, char in enumerate(normalized_text):
        rows[i % num_rows] += char
    
    if len(rows[-1]) < num_columns:
        rows[-1] += ' ' * (num_columns - len(rows[-1]))
    
    columns = [''.join(row) for row in zip(*rows)]
    encoded_text = ' '.join(columns)
    
    return encoded_text
