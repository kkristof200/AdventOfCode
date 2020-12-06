from typing import List

def f1(groups: List[List[str]]) -> None:
    print('f1:', sum([len(l) for l in groups]))

from input_loader import load_input

groups = [[[str(c) for c in group_line] for group_line in group.strip.split('\n')] for group in load_input().split('\n\n')]

print(groups)

# f1(groups)