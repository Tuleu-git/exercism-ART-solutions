COLORS = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
]

def label(colors: list[str]) -> str:

    # 33 ohms
    # 2 kiloohms = 2_000
    # 67 megaohms = 67_000_000
    # 99 gigaohms = 99_000_000_000

    number = (COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])) * 10 ** COLORS.index(colors[2])

    word = 'ohms'
    if number % 1000 == 0:
        word = 'kiloohms'
        number //= 1000
    if number % 1000 == 0:
        word = 'megaohms'
        number //= 1000
    if number % 1000 == 0:
        word = 'gigaohms'
        number //= 1000
        
    return f'{number} {word}' if number else '0 ohms'
    
