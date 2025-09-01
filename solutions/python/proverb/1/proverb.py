def proverb(*args: list[str], qualifier: str) -> list[str]:
    if not args:
        return []
    res = []
    length = len(args)
    
    if length > 1:
        for index in range(length -1):
            res.append(f'For want of a {args[index]} the {args[index +1]} was lost.')
        
    if qualifier:
        res.append(f'And all for the want of a {qualifier} {args[0]}.')
    else:
        res.append(f'And all for the want of a {args[0]}.')
        
    return res
