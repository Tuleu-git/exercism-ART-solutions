def reverse(text: str) -> str:
    new_text = ''
    for index in range(len(text) -1, -1, -1):
        new_text += text[index]
    return new_text
