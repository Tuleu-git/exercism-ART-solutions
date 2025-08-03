def square_root(number: int) -> int:
    for i in range(1, number + 1):
        if i * i == number:
            return i
