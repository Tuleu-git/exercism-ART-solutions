def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    
    data = {}
    for key, val in legacy_data.items():
        for letter in val:
            data[letter.lower()] = key

    return data