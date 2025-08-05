ACTIONS = {
    1: 'wink',
    2: 'double blink',
    4: 'close your eyes',
    8: 'jump'
}

def commands(binary_str: str) -> list[str]:
    binary_num = int(binary_str, 2)
    actions = [act for num, act in ACTIONS.items() if binary_num & num]

    return actions[::-1] if binary_num & 16 else actions
