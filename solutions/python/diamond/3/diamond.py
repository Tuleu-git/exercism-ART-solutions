ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rows(letter: str) -> list[str]:
    result = []
    index = ALPHABET.index(letter)
    if index == 0:
        return ['A']
    result.append(' ' * index + 'A' + ' ' * index)
    for i in range(index):
        result.insert(i + 1, ' ' * (index - i - 1) + 
                      f'{ALPHABET[i + 1]}' + 
                      ' ' * (i * 2 + 1) + 
                      f'{ALPHABET[i + 1]}' + 
                      ' ' * (index - i - 1))
    result = result[:-1] + result[::-1]
    return result
