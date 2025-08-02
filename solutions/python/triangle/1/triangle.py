def equilateral(lst: list[int]) -> bool:
    return (lst[0] + lst[1] >= lst[2] > 0 and lst[1] + lst[2] >= lst[0] > 0 and lst[0] + lst[2] >= lst[1] > 0) and lst[0] == lst[1] == lst[2] and lst[0] == lst[2]

def isosceles(lst: list[int]) -> bool:
    return (lst[0] + lst[1] >= lst[2] > 0 and lst[1] + lst[2] >= lst[0] > 0 and lst[0] + lst[2] >= lst[1] > 0) and (lst[0] == lst[1] or lst[1] == lst[2] or lst[0] == lst[2])

def scalene(lst: list[int]) -> bool:
    return (lst[0] + lst[1] >= lst[2] > 0 and lst[1] + lst[2] >= lst[0] > 0 and lst[0] + lst[2] >= lst[1] > 0) and lst[0] != lst[1] != lst[2] and lst[0] != lst[2]
