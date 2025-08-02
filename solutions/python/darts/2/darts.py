def score(x: int, y: int) -> int:
    squared_distance = x ** 2 + y ** 2
    return (squared_distance <= 1) * 5 + (squared_distance <= 25) * 4 + (squared_distance <= 100)