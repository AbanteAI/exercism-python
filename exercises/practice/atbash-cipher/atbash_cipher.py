from string import ascii_lowercase as asc_low

ENCODING = {chr: asc_low[id] for id, chr in enumerate(asc_low[::-1])}

def encode(text: str, decode: bool = False):
    res = "".join(ENCODING.get(chr, chr) for chr in text.lower() if chr.isalnum())
    return res if decode else " ".join(res[index:index+5] for index in range(0, len(res), 5))

def decode(text: str):
    return encode(text, True)