def is_armstrong_number(number: int) -> bool:
    return number == sum([int(n) ** len(str(number)) for n in str(number)])
