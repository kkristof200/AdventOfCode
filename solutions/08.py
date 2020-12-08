import copy
from typing import List, Tuple

def parse_command(cmd: str) -> Tuple[str, int]:
    comps = cmd.split(' ')

    return comps[0], int(comps[1])

def run(commmands: List[Tuple[str, int]], correct_duplicate: bool) -> int:
    accumulator = 0
    last_i = 0
    i = 0
    max_limit_i = len(commmands)
    used_positions = []

    while i < max_limit_i:
        if i in used_positions:
            if correct_duplicate:
                failed_command, failed_value = commmands[last_i]
                commmands[last_i] = ('jmp' if failed_command == 'nop' else 'nop', failed_value)

                return run(commmands, correct_duplicate=False)
            break

        used_positions.append(i)
        cmd, value = commands[i]
        last_i = i

        if cmd == 'acc':
            accumulator += value
        elif cmd == 'jmp':
            i += value

            continue

        i += 1
    
    return accumulator

def f1(commmands: List[Tuple[str, int]]) -> None:
    print(run(commmands, correct_duplicate=False))

def f2(commmands: List[Tuple[str, int]]) -> None:
    print(run(commmands, correct_duplicate=True))

from input_loader import load_input

commands = [parse_command(cmd.strip()) for cmd in load_input().split('\n')]

f1(commands)
f2(commands)