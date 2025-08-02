def is_isogram(string: str) -> bool:
    string = string.replace(' ', '').lower().replace('-', '')
    return len(string) == len(set(string))
