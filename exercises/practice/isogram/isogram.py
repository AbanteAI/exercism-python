def is_isogram(string):
    scrubbed = string.replace('-', '').replace(' ', '').lower()
    return len(scrubbed) == len(set(scrubbed))