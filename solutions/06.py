from typing import List

def f1(groups: List[List[str]]) -> None:
    print('f1:', sum([len(l) for l in groups]))

from input_loader import load_input

groups = [list({str(c) for c in group.replace('\n', '')}) for group in load_input().split('\n\n')]

f1(groups)