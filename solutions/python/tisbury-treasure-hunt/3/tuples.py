def get_coordinate(record: tuple[str, str]) -> str:
    return record[1]

def convert_coordinate(coordinate: str) -> tuple[str, str]:
    return coordinate[0], coordinate[1]

def compare_records(azara_record: tuple[str, str], rui_record: tuple[str, ...]) -> bool:
    return convert_coordinate(azara_record[1]) == rui_record[1]

def create_record(azara_record: tuple[str, str], rui_record: tuple[str, ...]) -> tuple[str, ...] | str:
    return azara_record + rui_record if compare_records(azara_record, rui_record) else 'not a match'

def clean_up(combined_record_group: tuple[tuple[str, ...], ...]) -> str:
    return '\n'.join(f'{(r[0], r[2], r[3], r[4])}' for r in combined_record_group) + '\n'
