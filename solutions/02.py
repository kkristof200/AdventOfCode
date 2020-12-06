from typing import List

# PART 1
def f1(lines: List[str]) -> None:
    valid = []
    invalid = []

    for l in lines:
        comps = l.split(':')
        pw = comps[1].strip()
        rules = comps[0].split(' ')
        rule_char = rules[1]
        rule_char_count = rules[0].split('-')
        rule_char_min = int(rule_char_count[0])
        rule_char_max = int(rule_char_count[1])

        char_occurence = len([c for c in pw if str(c) == rule_char])

        if char_occurence >= rule_char_min and char_occurence <= rule_char_max:
            valid.append(pw)
        else:
            invalid.append(pw)

    print('f1: valid  ', len(valid))
    print('f1: invalid', len(invalid))

# PART 2
def f2(lines: List[str]) -> None:
    valid = []
    invalid = []

    for l in lines:
        comps = l.split(':')
        pw = comps[1].strip()
        rules = comps[0].split(' ')
        rule_char = rules[1]
        rule_char_count = rules[0].split('-')
        rule_char_pos_1 = int(rule_char_count[0]) - 1
        rule_char_pos_2 = int(rule_char_count[1]) - 1

        contains_pos_1 = len(pw) > rule_char_pos_1 and str(pw[rule_char_pos_1]) == rule_char
        contains_pos_2 = len(pw) > rule_char_pos_2 and str(pw[rule_char_pos_2]) == rule_char

        if contains_pos_1 ^ contains_pos_2:
            valid.append(pw)
        else:
            invalid.append(pw)

    print('f2: valid  ', len(valid))
    print('f2: invalid', len(invalid))

from input_loader import load_input

lines = load_input().split('\n')

f1(lines)
f2(lines)