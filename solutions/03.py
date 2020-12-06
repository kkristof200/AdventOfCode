from typing import List

def get_tree_count(a: List[List[str]], step_x: int, step_y: int) -> int:
    x, y = 0, 0
    count = 0

    while y < h-step_y:
        y += step_y
        x += step_x

        if x >= w:
            x -= w
        
        if a[y][x] == '#':
            count += 1
    
    return count

def f1(trees: List[List[str]]) -> None:
    print('f1:', get_tree_count(trees, 3, 1))

def f2(trees: List[List[str]]) -> None:
    inputs = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    res = 1

    for inp in inputs:
        step_x, step_y = inp
        res *= get_tree_count(trees, step_x, step_y)

    print('f2:', res)

    
from input_loader import load_input

lines = load_input().split('\n')
h = len(lines)
w = len(lines[0])
trees = [[str(c) for c in line] for line in lines]

f1(trees)
f2(trees)