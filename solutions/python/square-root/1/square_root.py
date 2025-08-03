def square_root(number: int) -> int:
    L, R = 0, number
    while L <= R:
        middle = (L + R) // 2
        if middle * middle == number:
            return middle
        elif middle * middle > number:
            R = middle - 1
        else:
            L = middle + 1
