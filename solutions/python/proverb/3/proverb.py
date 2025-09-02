def proverb(*args: list[str], qualifier: str | None = None) -> list[str]:
    if not args:
        return []

    res = [
        f'For want of a {args[index]} the {args[index +1]} was lost.'
        for index in range(len(args) -1)
    ]

    last = f'{qualifier} {args[0]}' if qualifier else args[0]
    res.append(f'And all for the want of a {last}.')
        
    return res
