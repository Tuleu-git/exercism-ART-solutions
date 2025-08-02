CARD_VALUES = {
    'A': 1, 'J': 10, 'Q': 10, 'K': 10, '10': 10, 
    '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
}

def value_of_card(card: str) -> int:
    return CARD_VALUES[card]

def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    if CARD_VALUES[card_one] == CARD_VALUES[card_two]:
        return card_one, card_two
    return card_one if CARD_VALUES[card_one] > CARD_VALUES[card_two] else card_two

def value_of_ace(card_one: str, card_two: str) -> int:
    if card_one == 'A' or card_two == 'A':
        return 1
    else:
        return 11 if CARD_VALUES[card_one] + CARD_VALUES[card_two] <= 10 else 1

def is_blackjack(card_one: str, card_two: str) -> bool:
    return (card_one == 'A' and CARD_VALUES[card_two] == 10) or (card_two == 'A' and CARD_VALUES[card_one] == 10)

def can_split_pairs(card_one: str, card_two: str) -> bool:
    return CARD_VALUES[card_one] == CARD_VALUES[card_two]

def can_double_down(card_one: str, card_two: str) -> bool:
    return 9 <= CARD_VALUES[card_one] + CARD_VALUES[card_two] <= 11