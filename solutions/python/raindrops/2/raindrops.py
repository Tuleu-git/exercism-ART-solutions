def convert(number: int) -> str:
    lst = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    return ''.join(a for b, a in lst if not number % b) or str(number)