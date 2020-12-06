from typing import List

def parse_passport(passport_str: str) -> dict:
    comps = [e.strip().split(':') for e in passport_str.split(' ')]

    return {e[0]:e[1] for e in comps}

def is_passport_valid_v1(passport: dict, needed_keys: List[str]) -> bool:
    existing_keys = list(passport.keys())

    for needed_key in needed_keys:
        if needed_key not in existing_keys:
            return False

    return True

def is_passport_valid_v2(passport: dict, needed_keys: List[str]) -> bool:
    existing_keys = list(passport.keys())

    for key in needed_keys:
        try:
            if key not in existing_keys:
                return False

            val = passport[key]

            if key == 'byr':
                int_val = int(val)

                if len(val) != 4 or int_val < 1920 or int_val > 2002:
                    return False
            elif key == 'iyr':
                int_val = int(val)

                if len(val) != 4 or int_val < 2010 or int_val > 2020:
                    return False
            elif key == 'eyr':
                int_val = int(val)

                if len(val) != 4 or int_val < 2020 or int_val > 2030:
                    return False
            elif key == 'hgt':
                if not val.endswith('cm') and not val.endswith('in'):
                    return False

                is_cm = 'cm' in val
                int_val = int(val.replace('cm' if is_cm else 'in', ''))
                min_val = 150 if is_cm else 59
                max_val = 193 if is_cm else 76

                if int_val < min_val or int_val > max_val:
                    return False
            elif key == 'hcl':
                if not val.startswith('#') or len(val) != 7:
                    return False

                _val = val.replace('#', '', 1)
                filtered_val_comps = [c for c in _val if str(c) in '0123456789abcdef']

                if len(filtered_val_comps) != 6:
                    return False
            elif key == 'ecl':
                if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    return False
            elif key == 'pid':
                if len(val) != 9 or int(val) < 0:
                    return False
        except Exception as e:
            print(key, e)
            return False

    return True


def f1(passports: List[dict], needed_keys: List[str]) -> None:
    print('f1:', len([p for p in passports if is_passport_valid_v1(p, needed_keys)]))

def f2(passports: List[dict], needed_keys: List[str]) -> None:
    print('f1:', len([p for p in passports if is_passport_valid_v2(p, needed_keys)]))


from input_loader import load_input

inp = load_input()
passport_strs = [p.strip().replace('\n', ' ') for p in inp.split('\n\n')]
passports = [parse_passport(passport_str) for passport_str in passport_strs]

needed_keys = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']


f1(passports, needed_keys)
f2(passports, needed_keys)