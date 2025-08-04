def encode(plain_text: str) -> str:
    formatting = str.maketrans(
        'abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper(), 'zyxwvutsrqponmlkjihgfedcba' + 'zyxwvutsrqponmlkjihgfedcba'
    )
    plain_text = plain_text.translate(formatting).replace(' ', '').replace('.', '').replace(',', '')
    list = []
    for index, letter in enumerate(plain_text):
        if (index + 1) % 5 == 0:
            list.append(f'{letter} ')
        else:
            list.append(letter)
    return ''.join(list).strip()

def decode(ciphered_text: str) -> str:
    return ''.join(map(encode, ciphered_text))
