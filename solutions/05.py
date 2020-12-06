from typing import List

def get_pos(indicators: List[str], count: int) -> int:
    _range = [0, count - 1]

    for e in indicators:
        next_range = round((_range[1] - _range[0]) / 2)

        if e in ['F', 'L']:
            _range[1] -= next_range
        else:
            _range[0] += next_range

    return _range[0] if e in ['F', 'L'] else _range[1]


def f1(seat_codes: List[str], row_count: int, column_count: int) -> None:
    max_seat_id = 0

    for seat_code in seat_codes:
        row = get_pos([str(s) for s in seat_code[:7]], row_count)
        column = get_pos([str(s) for s in seat_code[7:]], column_count)

        seat_id = row * 8 + column

        if seat_id > max_seat_id:
            max_seat_id = seat_id

    print('f1: max_seat_id =', max_seat_id)

def f2(seat_codes: List[str], row_count: int, column_count: int) -> None:
    seats = [[0 for _ in range(column_count)] for _ in range(row_count)]

    for seat_code in seat_codes:
        row = get_pos([str(s) for s in seat_code[:7]], row_count)
        column = get_pos([str(s) for s in seat_code[7:]], column_count)
        seats[row][column] = 1

    missing_positions = [[(row, column) for column in range(column_count) if seats[row][column] == 0] for row in range(row_count)]
    missing_positions = [row for row in missing_positions if len(row) == 1]
    missing_position = missing_positions[0][0]
    print('f2: missing_position =', missing_position, 'id =', missing_position[0] * 8 + missing_position[1])

from input_loader import load_input

seat_codes = load_input().split('\n')


ROW_COUNT = 128
COLUMN_COUNT = 8

f1(seat_codes, ROW_COUNT, COLUMN_COUNT)
f2(seat_codes, ROW_COUNT, COLUMN_COUNT)