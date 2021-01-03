from typing import List, Dict, Tuple


def is_valid(pwd: str, policy: Dict[str, List]) -> bool:
    valid = False
    chars = {}
    for char in pwd:
        if char in policy:
            if char in chars:
                chars[char]['count'] += 1
            else:
                chars[char] = {'count': 1}

            chars[char]['valid'] = True
            count = chars[char]['count']
            min_chars, max_chars = policy[char][0], policy[char][1]
            if count < min_chars or count > max_chars:
                chars[char]['valid'] = False

    if len(chars) == 0:  # invalid: no items from policy found in pass
        return False

    for k, v in chars.items():
        if v['valid'] == False:
            return False
    return True


def is_valid_pos(pwd: str, policy: Dict[str, List]) -> bool:
    char = list(policy.keys())[0]  # could contain multiple policies
    pos_1, pos_2 = policy[char]
    pos_1, pos_2 = pos_1 - 1, pos_2 - 1  # make positions zero indexed
    return (pwd[pos_1] == char) ^ (pwd[pos_2] == char)


def parse_policy(policy: str) -> Dict[str, List]:
    qty, char = policy.split(' ')
    min_chars, max_chars = qty.split('-')
    min_chars, max_chars = int(min_chars), int(max_chars)
    return {char: [min_chars, max_chars]}


def parse_password(pwd_with_policy: str) -> Tuple[str, Dict[str, List]]:
    policy, pwd = pwd_with_policy.split(': ')
    return pwd, parse_policy(policy)


def count_valid(pwds: List[Tuple[str, Dict[str, List]]]) -> int:
    count = 0
    for pwd, policy in pwds:
        if is_valid_pos(pwd, policy):
            count += 1
    return count


if __name__ == '__main__':
    f = open('input.txt', 'r')
    pwds: List[Tuple[str, Dict[str, List]]] = []
    for line in f:
        pwd, policy = parse_password(line)
        pwds.append((pwd, policy))

    valid_count = count_valid(pwds)
    print('there are {} valid passwords in the input file.'.format(valid_count))
    f.close()
