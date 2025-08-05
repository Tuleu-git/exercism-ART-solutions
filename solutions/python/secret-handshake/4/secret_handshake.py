ACTIONS = {
    1: 'wink',
    2: 'double blink',
    4: 'close your eyes',
    8: 'jump'
}

def commands(binary_str: str) -> list[str]:
    return [act for num, act in ACTIONS.items() if int(binary_str, 2) & num][::-1] if int(binary_str, 2) & 16 else [act for num, act in ACTIONS.items() if int(binary_str, 2) & num]
