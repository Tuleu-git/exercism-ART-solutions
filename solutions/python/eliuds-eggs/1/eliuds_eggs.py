def egg_count(display_value: int) -> int:
    display_value = bin(display_value)
    return display_value.count('1')
