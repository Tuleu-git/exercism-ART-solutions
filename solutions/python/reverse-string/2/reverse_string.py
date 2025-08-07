def reverse(text: str) -> str:
    new_text = ''
    for l in reversed(text):
        new_text += l
    return new_text
