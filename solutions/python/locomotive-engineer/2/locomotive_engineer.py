def get_list_of_wagons(*args: int) -> list[int]:
    return list(args)

def fix_list_of_wagons(each_wagons_id: list[int], missing_wagons: list[int]) -> list[int]:
    a, b, c, *res = each_wagons_id
    return [c, *missing_wagons, *res, a, b]

def add_missing_stops(route: dict[str, str], **kwargs) -> dict[str, str]:
    return {**route, 'stops': list(kwargs.values())}

def extend_route_information(route: dict[str, str], more_route_information: dict[str, str]) -> dict[str, str]:
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows: list[list[tuple]]) -> list[list[tuple]]:
    return [list(row) for row in zip(*wagons_rows)]