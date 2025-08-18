DAYS = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]

GIFTS = [
    'and a Partridge in a Pear Tree.',
    'two Turtle Doves, ',
    'three French Hens, ',
    'four Calling Birds, ',
    'five Gold Rings, ',
    'six Geese-a-Laying, ',
    'seven Swans-a-Swimming, ',
    'eight Maids-a-Milking, ',
    'nine Ladies Dancing, ',
    'ten Lords-a-Leaping, ',
    'eleven Pipers Piping, ',
    'twelve Drummers Drumming, '
]

def recite(start_verse: int, end_verse: int) -> str:
    if start_verse == end_verse:
        if start_verse == 1:
            return ['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.']

        final = []
        result = f'On the {DAYS[start_verse - 1]} day of Christmas my true love gave to me: '
        for i in range(end_verse -1, -1, -1):
            result += GIFTS[i]
        final.append(result)
    else:
        final = []
        if start_verse == 1:
            final.append('On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.')
            start_verse += 1
        for n in range(start_verse, end_verse + 1):
            result = f'On the {DAYS[n - 1]} day of Christmas my true love gave to me: '
            for i in range(n -1, -1, -1):
                result += GIFTS[i]
            final.append(result)
    
    return final