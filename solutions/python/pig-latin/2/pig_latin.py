def translate(text: str) -> str | type:
    if text.find(" ") != -1:
        return ' '.join(map(translate_one, text.split()))
    else:
        return translate_one(text)
def translate_one(text: str) -> str | type:
    lst1 = ("a", "e", "i", "o", "u")
    lst2 = ("xr", "yt")
    if text.startswith(lst1) or text.startswith(lst2):
        return text + 'ay'
    if (q := text.find("qu")) != -1 and not any(v in text[:q+1] for v in lst1):
        return text[q+2:] + text[:q+2] + 'ay'
    if (q := text.find("y")) > 0 and not any(v in text[:q+1] for v in lst1):
        return text[q:] + text[:q] + 'ay'
    else:
        if any(v in text for v in lst1):
            q = next((i for i, l in enumerate(text) if l in lst1))
            return text[q:] + text[:q] + 'ay'
        raise ValueError