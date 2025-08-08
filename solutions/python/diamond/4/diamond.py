ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rows(letter: str) -> list[str]:
    result = []
    index = ALPHABET.index(letter)
    if index == 0:
        return ['A']
    result.append('A'.center(index * 2 + 1))
    for i in range(index):
        middle = f'{ALPHABET[i + 1]}{" " * (i * 2 + 1)}{ALPHABET[i + 1]}'
        result.insert(i + 1, middle.center(len(middle) + (index - 1 - i) * 2))
    result = result[:-1] + result[::-1]
    return result
