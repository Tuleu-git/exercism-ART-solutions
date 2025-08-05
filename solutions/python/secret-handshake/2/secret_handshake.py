ACTIONS = [
    'jump',
    'close your eyes',
    'double blink',
    'wink'
]

def commands(binary_str: str) -> list[str]:
    actions = []
    for index, digit in enumerate(binary_str[1:]):
        if digit == '1':
            actions.append(ACTIONS[index])
    return actions if binary_str[0] == '1' else actions[::-1]
