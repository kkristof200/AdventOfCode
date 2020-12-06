from typing import List, Dict

def get_group_occurences(group: List[List[str]]) -> Dict[str, int]:
    # LONG
    # occurences = {}

    # for group_line in group:
    #     for char in group_line:
    #         if char not in occurences:
    #             occurences[char] = 0

    #         occurences[char] += 1

    # SHORT
    flattened_list = [s for s in group for s in s]

    return {c:flattened_list.count(c) for c in flattened_list}

def f1(groups: List[List[List[str]]]) -> None:
    # LONG
    # score = 0

    # for group in groups:
    #     for count in get_group_occurences(group).values():
    #         score += 1

    # print('f1:', score)

    # SHORT
    print('f1:', sum([len(get_group_occurences(group).keys()) for group in groups]))

def f2(groups: List[List[List[str]]]) -> None:
    # LONG
    # score = 0

    # for group in groups:
    #     needed_count = len(group)

    #     for count in get_group_occurences(group).values():
    #         if count == needed_count:
    #             score += 1

    # print('f2:', score)

    # SHORT
    print('f2:', sum([len(['*' for answer_count in occurence.values() if answer_count == responders]) for responders, occurence in [(len(group), get_group_occurences(group)) for group in groups]]))


from input_loader import load_input

groups = [[[str(c) for c in group_line] for group_line in group.split('\n')] for group in load_input().split('\n\n')]


f1(groups)
f2(groups)