def parse_rule(rule: str) -> (str, dict):
    comps = [s.strip() for s in rule.replace('bags', '').replace('bag', '').rstrip('.').split('contain')]
    holder_bag = comps[0]

    if comps[1] == 'no other':
        return holder_bag, {}

    contained_bags = {}

    for held_bag_str in [s.strip() for s in comps[1].split(',')]:
        _comps = [s.strip() for s in held_bag_str.split(' ', 1)]
        contained_bags[_comps[1]] = int(_comps[0])

    return holder_bag, contained_bags

def get_rules(rule_strs: list) -> dict:
    rules = {}

    for rule_str in rule_strs:
        holder_bag, contained_bags = parse_rule(rule_str)
        rules[holder_bag] = contained_bags

    return rules

def get_parents(rules: dict, bag_color: list) -> list:
    parent_colors = []

    for parent_color in [parent_color for parent_color, child_colors in rules.items() if bag_color in child_colors]:
        parent_colors.extend([parent_color] + [_parent_color for _parent_color in get_parents(rules, parent_color)])

    _parent_colors = []

    for _parent_color in parent_colors:
        if _parent_color not in _parent_colors:
            _parent_colors.append(_parent_color)

    return _parent_colors

def get_bag_count(rules: dict, bag_color: str) -> int:
    child_colors_counts = rules[bag_color]
    count = 0

    for child_bag_color, child_bag_count in rules[bag_color].items():
        count += child_bag_count + child_bag_count * get_bag_count(rules, child_bag_color)

    return count


def f1(rules: dict, target_bag_color: str) -> None:
    print(len(get_parents(rules, target_bag_color)))

def f2(rules: dict, target_bag_color: str) -> None:
    print(get_bag_count(rules, target_bag_color))


from kcu import kjson
from input_loader import load_input

rules = get_rules(load_input().split('\n'))
TARGET_BAG_COLOR = 'shiny gold'

f1(rules, TARGET_BAG_COLOR)
f2(rules, TARGET_BAG_COLOR)