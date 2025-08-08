ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rows(letter: str) -> list[str]:
    index = ALPHABET.index(letter)
    if index == 0:
        return ['A']
    
    result = []
    max_width = index * 2 + 1
    
    result.append('A'.center(max_width))
    for i in range(index):
        char = ALPHABET[i + 1]
        middle = f'{char}{" " * (i * 2 + 1)}{char}'
        result.append(middle.center(max_width))
    
    result = result[:-1] + result[::-1]
    return result
