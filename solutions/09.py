from typing import List, Optional, Tuple

def get_sum_comps(numbers: List[int], sum: int) -> Optional[Tuple[int, int]]:
    for num1 in numbers:
        num2 = sum - num1

        if num2 in numbers:
            return num1, num2

    return None

def find_contagious_num(numbers: List[int], sample_size: int) -> Optional[Tuple[int, int]]:
    for start_pos in range(len(numbers) - sample_size):
        end_pos = start_pos + sample_size
        sum_comps = get_sum_comps(numbers[start_pos: end_pos], numbers[end_pos])

        if not sum_comps:
            return end_pos, numbers[end_pos]

    return None

def f1(numbers: List[int], sample_size: int) -> None:
    _, num = find_contagious_num(numbers, sample_size)

    print('f1:   ', num)

def f2_v1(numbers: List[int], sample_size: int) -> None:
    pos, num = find_contagious_num(numbers, sample_size)

    for start_pos in range(pos):
        for end_pos in range(start_pos+3, pos+1):
            if sum(numbers[start_pos:end_pos]) == num:
                sorted_val = sorted(numbers[start_pos:end_pos])
                print('f2_v1:', sorted_val[0] + sorted_val[-1])

                return

def f2_v2(numbers: List[int], sample_size: int) -> None:
    pos, num = find_contagious_num(numbers, sample_size)

    for i in range(3, pos):
        l = pos - i

        for start_pos in range(pos-l):
            end_pos = start_pos + l

            if sum(numbers[start_pos:end_pos]) == num:
                sorted_val = sorted(numbers[start_pos:end_pos])
                print('f2_v2:', sorted_val[0] + sorted_val[-1])

                return

from input_loader import load_input

NUMBERS = [int(num_str.strip()) for num_str in load_input().split('\n')]
SAMPLE_SIZE = 25

f1(NUMBERS, SAMPLE_SIZE)
f2_v1(NUMBERS, SAMPLE_SIZE)
f2_v2(NUMBERS, SAMPLE_SIZE)