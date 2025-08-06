BRACKETS = {
    '{': '}',
    '[': ']',
    '(': ')'
}

def is_paired(input_string: str) -> bool:
    stack = []
    for l in input_string:
        if l in BRACKETS:
            stack.append(l)
        elif l in BRACKETS.values():
            if not stack or BRACKETS[stack.pop()] != l:
                return False
    return not stack