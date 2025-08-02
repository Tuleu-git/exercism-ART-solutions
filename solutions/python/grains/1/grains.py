def square(n):
    if not 0 < n < 65:
        raise ValueError("square must be between 1 and 64")
    return 2 **(n-1)

def total():
    return sum([1 << i for i in range(64)])