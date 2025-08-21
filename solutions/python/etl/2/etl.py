def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    return {
        letter.lower(): key
        for key, val in legacy_data.items()
        for letter in val
    }