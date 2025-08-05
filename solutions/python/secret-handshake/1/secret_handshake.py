ACTIONS = [
    'jump',
    'close your eyes',
    'double blink',
    'wink'
]

def commands(binary_str: str) -> list[str]:
    actions = []
    n = 0
    for i in binary_str[1:]:
        if i == '1':
            actions.append(ACTIONS[n])
        n += 1
    if binary_str[0] == '1':
        return actions
    return actions[::-1]
