ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rows(letter: str) -> list[str]:
    result = []
    index = ALPHABET.index(letter)
    if index == 0:
        return ['A']
    result.append(' ' * index + 'A' + ' ' * index)
    result.append(' ' * index + 'A' + ' ' * index)
    for i in range(index - 1):
        result.insert(i + 1, ' ' * (index - i - 1) + 
                      f'{ALPHABET[i + 1]}' + 
                      ' ' * (i * 2 + 1) + 
                      f'{ALPHABET[i + 1]}' + 
                      ' ' * (index - i - 1))
        result.insert(i + 1, ' ' * (index - i - 1) + 
                      f'{ALPHABET[i + 1]}' + 
                      ' ' * (i * 2 + 1) + 
                      f'{ALPHABET[i + 1]}' + 
                      ' ' * (index - i - 1))
    result.insert(index, f'{letter}' + ' ' * (index * 2 - 1) + f'{letter}')
    return result
