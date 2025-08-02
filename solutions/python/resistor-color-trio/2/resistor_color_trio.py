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

UNIT = [
    (1_000_000_000, 'gigaohms'),
    (1_000_000, 'megaohms'),
    (1_000, 'kiloohms'),
    (1, 'ohms')
]

def label(colors: list[str]) -> str:

    value = (COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])) * 10 ** COLORS.index(colors[2])

    if value == 0:
        return '0 ohms'
    
    for scale, unit in UNIT:
        if value % scale == 0:
            return f'{value // scale} {unit}'
