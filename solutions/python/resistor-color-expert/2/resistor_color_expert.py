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

TOLERANCE = {
    'grey': 0.05,
    'violet': 0.1,
    'blue': 0.25,
    'green': 0.5,
    'brown': 1,
    'red': 2,
    'gold': 5,
    'silver': 10
}

def resistor_label(colors: list[str]) -> str:
    length = len(colors)

    if length == 1:
        return '0 ohms'

    elif length == 4:
        value = COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])
        value *= 10 ** COLORS.index(colors[2])
        tolerance = TOLERANCE[colors[3]]
    elif length == 5:
        value = COLORS.index(colors[0]) * 100 + COLORS.index(colors[1]) * 10 + COLORS.index(colors[2])
        value *= 10 ** COLORS.index(colors[3])
        tolerance = TOLERANCE[colors[4]]

    for scale, unit in UNIT:
        if value >= scale:
            scaled_value = value / scale
            if scaled_value.is_integer():
                return f'{int(scaled_value)} {unit} ±{tolerance}%'
            return f'{scaled_value} {unit} ±{tolerance}%'
