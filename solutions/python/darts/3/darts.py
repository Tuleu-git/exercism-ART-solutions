def score(x: int, y: int) -> int:
    squared_distance = x ** 2 + y ** 2
    return 10 if squared_distance <= 1 else 5 if squared_distance <= 25 else 1 if squared_distance <= 100 else 0