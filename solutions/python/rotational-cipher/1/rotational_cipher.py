Plain = 'abcdefghijklmnopqrstuvwxyz'

def rotate(text: str, key: int) -> str:
    new_text = ''
    Cipher = Plain[key:] + Plain[:key]
    for l in text:
        if not l.isalpha():
            new_text += l
        elif l.isupper():
            new_text += Cipher[Plain.find(l.lower())].upper()
        else:
            new_text += Cipher[Plain.find(l)]
    
    return new_text