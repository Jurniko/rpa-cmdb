import unicodedata as und

def str_unformat(str):
    nw_str = und.normalize('NFKD',str).translate(dict.fromkeys(map(ord, u'\u0300\u0301\u0302\u0308'), None))
    return nw_str.lower()

