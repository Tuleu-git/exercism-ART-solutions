LETTERS = 'abcdefghijklmnopqstuvwxyz'
def is_pangram(sentence: str) -> bool:
    return all(l in sentence.lower() for l in LETTERS)