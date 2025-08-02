def is_valid(isbn: str) -> bool: # 3-598-21507-X
    isbn = isbn.replace('-', '')
    if not len(isbn) == 10 or not isbn[:-1].isdigit() or (not isbn[-1].isdigit() and not isbn[-1] == 'X'):
        return False

    lst_isbn = [int(n) if n.isdigit() else 10 for n in isbn]

    num = lst_isbn[0] * 10 + lst_isbn[1] * 9 + lst_isbn[2] * 8 + lst_isbn[3] * 7 + lst_isbn[4] * 6 + lst_isbn[5] * 5 + lst_isbn[6] * 4 + lst_isbn[7] * 3 + lst_isbn[8] * 2 + lst_isbn[9]
    
    return num % 11 == 0