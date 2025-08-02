def get_rounds(number: int) -> list:
    return list(range(number, number+3))

def concatenate_rounds(rounds_1: list, rounds_2: list) -> list:
    return rounds_1 + rounds_2

def list_contains_round(rounds: list, number: int) -> bool:
    return number in rounds

def card_average(hand: list) -> float:
    return sum(hand)/len(hand)

def approx_average_is_average(hand: list) -> bool:
    return sum(hand) / len(hand) in ((hand[0] + hand[-1]) / 2, hand[len(hand) // 2])

def average_even_is_average_odd(hand: list) -> bool:
    return sum(hand[::2])/len(hand[::2]) == sum(hand[1::2])/len(hand[1::2])

def maybe_double_last(hand: list) -> list:
    return hand if hand[-1] != 11 else hand[:-1] + [22]
