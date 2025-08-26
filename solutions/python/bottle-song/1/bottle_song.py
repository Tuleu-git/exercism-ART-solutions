AMOUNT = [
    'no',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten'
]

def recite(start: int, take: int = 1) -> list[str]:
    result = []
    for bottle in range(start, start - take, -1):
        if bottle == 1:
            result.append("One green bottle hanging on the wall,")
            result.append("One green bottle hanging on the wall,")
        else:
            result.append(f"{AMOUNT[bottle].title()} green bottles hanging on the wall,")
            result.append(f"{AMOUNT[bottle].title()} green bottles hanging on the wall,")
        result.append(f"And if one green bottle should accidentally fall,",)
        if bottle == 2:
            result.append(f"There'll be one green bottle hanging on the wall.",)
        else:
            result.append(f"There'll be {AMOUNT[bottle -1]} green bottles hanging on the wall.")

        if bottle > start - take + 1:
            result.append("")

    return result