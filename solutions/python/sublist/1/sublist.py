SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one: list, list_two: list) -> int:
    len1 = len(list_one)
    len2 = len(list_two)
    
    if len1 == len2:
        return 3 if all([list_one[x] == list_two[x] for x in range(len1)]) else 4
    if list_one == []:
        return 1
    if list_two == []:
        return 2
    if len1 < len2:
        for i in range(len2):
            if list_one[0] == list_two[i]:
                if all([list_one[x] == list_two[x + i] for x in range(len1)]):
                    return 1
        return 4
    if len1 > len2:
        for i in range(len1):
            if list_two[0] == list_one[i]:
                if all([list_two[x] == list_one[x + i] for x in range(len2)]):
                    return 2
        return 4
