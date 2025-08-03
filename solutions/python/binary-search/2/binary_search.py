def find(search_list: list[int], value: int) -> int:
    if not search_list or value < search_list[0] or value > search_list[-1]:
        raise ValueError("value not in array")
    
    L, R = 0, len(search_list) -1
    while L <= R:
        index = (L + R) // 2
        middle = search_list[index]
        if middle == value:
            return index
        elif middle > value:
            R = index - 1
        else:
            L = index + 1
    raise ValueError("value not in array")
