def triangle(lst: list[int]) -> bool:
    a, b, c = sorted(lst)
    return a + b > c

def equilateral(lst: list[int]) -> bool:
    return triangle(lst) and len(set(lst)) == 1

def isosceles(lst: list[int]) -> bool:
    return triangle(lst) and len(set(lst)) <= 2

def scalene(lst: list[int]) -> bool:
    return triangle(lst) and len(set(lst)) > 2
