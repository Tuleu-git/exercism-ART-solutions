LETTERS = {
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 
    'v', 'w', 'x', 'y', 'z'
}
def is_pangram(sentence: str) -> bool:
    return len([l for l in LETTERS if l in sentence.lower()]) == 26
