def proverb(*args: list[str], qualifier: str) -> list[str]:
    if not args:
        return []
    
    res = []
    for index in range(len(args) -1):
        res.append(f'For want of a {args[index]} the {args[index +1]} was lost.')

    last = f'{qualifier} {args[0]}' if qualifier else args[0]
    res.append(f'And all for the want of a {last}.')
        
    return res
