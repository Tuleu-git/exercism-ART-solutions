Plain = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text: str, key: int) -> str:
    Cipher = Plain[key:] + Plain[:key]
    formatting = str.maketrans(Plain + Plain.upper(), Cipher + Cipher.upper())
    return text.translate(formatting)