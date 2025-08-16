def get_coordinate(record: tuple[str]) -> str:
    return record[1]

def convert_coordinate(coordinate: str) -> tuple[str]:
    return tuple(crd for crd in coordinate)

def compare_records(azara_record: tuple[str], rui_record: tuple[str]) -> bool:
    return tuple(crd for crd in azara_record[1]) == rui_record[1]

def create_record(azara_record: tuple[str], rui_record: tuple[str]) -> tuple[str] | str:
    return azara_record + rui_record if compare_records(azara_record, rui_record) else 'not a match'

def clean_up(combined_record_group: tuple[tuple[str]]) -> str:
    report = []
    for record in combined_record_group:
        cleaned_record = (
            record[0],
            record[2],
            record[3],
            record[4]
        )
        report.append(f'{cleaned_record}')
    return '\n'.join(report) + '\n'
