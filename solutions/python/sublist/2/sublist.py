SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one: list, list_two: list) -> int:
    len1 = len(list_one)
    len2 = len(list_two)
    
    if list_one == list_two:
        return 3
    
    if len1 == 0:
        return 1
    if len2 == 0:
        return 2
    
    if len1 < len2:
        for i in range(len2 - len1 + 1):
            if list_two[i:i+len1] == list_one:
                return 1

    if len1 > len2:
        for i in range(len1 - len2 + 1):
            if list_one[i:i+len2] == list_two:
                return 2

    return 4
