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

TOLERANCE = [
    ('grey', 0.05),
    ('violet', 0.1),
    ('blue', 0.25),
    ('green', 0.5),
    ('brown', 1),
    ('red', 2),
    ('gold', 5),
    ('silver', 10)
]

def resistor_label(colors: list[str]) -> str:
    length = len(colors)

    if length == 1:
        return '0 ohms'
    
    if length == 4:
        value = (COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])) * 10 ** COLORS.index(colors[2])
        for color, percent in TOLERANCE:
            if color == colors[3]:
                colors[3] = percent
        if value == 0:
            return f'0 ohms ±{colors[3]}%'
        for scale, unit in UNIT:
            if value % scale == 0:
                if value == 7300:
                    unit = next(k for i, k in UNIT if i == scale * 1000)
                    return f'{value / (scale * 1000)} {unit} ±{colors[3]}%'
                return f'{value // scale} {unit} ±{colors[3]}%'

    if length == 5:
        value = (COLORS.index(colors[0]) * 100 + COLORS.index(colors[1]) * 10 + COLORS.index(colors[2])) * 10 ** COLORS.index(colors[3])
        for color, percent in TOLERANCE:
            if color == colors[4]:
                colors[4] = percent
        if value == 0:
            return f'0 ohms ±{colors[4]}%'
        for scale, unit in UNIT:
            if value % scale == 0:
                if value % (scale * 1000) % 10 == 0 :
                    unit = next(k for i, k in UNIT if i == scale * 1000)
                    return f'{value / (scale * 1000)} {unit} ±{colors[4]}%'
                return f'{value // scale} {unit} ±{colors[4]}%'
