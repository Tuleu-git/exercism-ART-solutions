PLAIN = 'abcdefghijklmnopqrstuvwxyz'
CIPHER = PLAIN[::-1]

def encode(plain_text: str) -> str:
    formatting = str.maketrans(PLAIN + PLAIN.upper(), CIPHER * 2)
    plain_text = ''.join(l for l in plain_text if l.isalnum())
    plain_text = plain_text.translate(formatting)

    return ' '.join(plain_text[i : i + 5] for i in range(0, len(plain_text), 5))

def decode(ciphered_text: str) -> str:
    return ''.join(map(encode, ciphered_text))
