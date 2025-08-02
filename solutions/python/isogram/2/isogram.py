def is_isogram(string: str) -> bool:
    string = [l for l in string.lower() if l.isalpha()]
    return len(string) == len(set(string))
