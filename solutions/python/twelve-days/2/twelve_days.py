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
    'a Partridge in a Pear Tree.',
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

def recite(start_verse: int, end_verse: int) -> list[str]:
    verses = []
    for day in range(start_verse, end_verse +1):
        verse = f'On the {DAYS[day - 1]} day of Christmas my true love gave to me: '

        gifts = []
        for a_gift in range(day -1, 0, -1):
            gifts.append(GIFTS[a_gift])

        if day == 1:
            verse += GIFTS[0]
        else:
            verse += ''.join(gifts) + 'and ' + GIFTS[0]

        verses.append(verse)

    return verses