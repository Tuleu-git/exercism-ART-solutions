def is_valid(isbn: str) -> bool: # 3-598-21507-X
    lst = list(isbn.replace('-', ''))
    if len(lst) != 10: return False
    if lst[-1] == 'X': lst[-1] = '10'
    if not all([n.isdigit() for n in lst]): return False
    return sum([int(a) * b for a, b in zip(lst, range(10, 0, -1))]) % 11 == 0