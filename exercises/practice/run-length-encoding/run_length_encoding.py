import re


def decode(string):
    decoded = ""
    for count, char in re.findall(r"(\d*)(\D)", string):
        decoded += char * int(count or 1)
    return decoded


def encode(string):
    encoded = ""
    for char, group in re.findall(r"((\D)\2*)", string):
        count = len(group)
        encoded += f"{count if count > 1 else ''}{char}"
    return encoded