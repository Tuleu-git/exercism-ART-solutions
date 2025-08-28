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
    for bottle in range(take):
        verse = f"{AMOUNT[start - bottle].title()} green bottles hanging on the wall,"
        if start - bottle == 1:
            verse = "One green bottle hanging on the wall,"
        
        last_line = f"There'll be {AMOUNT[start - bottle -1]} green bottles hanging on the wall."
        if start - bottle == 2:
            last_line = "There'll be one green bottle hanging on the wall."
        
        result.append(verse)
        result.append(verse)
        result.append("And if one green bottle should accidentally fall,")
        result.append(last_line)

        if bottle < take -1:
            result.append("")

    return result