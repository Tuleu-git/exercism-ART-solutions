def score(x, y):
    squared_distance = x ** 2 + y ** 2
    if squared_distance <= 1:
        return 10
    if squared_distance <= 25:
        return 5
    if squared_distance <= 100:
        return 1
    return 0