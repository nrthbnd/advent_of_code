import re


def read_input() -> str:
    with open('input_2.txt', 'r') as file:
        input_string = file.read()
    return input_string


def find_muls(input_string: str) -> list:
    muls = []
    blocks = re.split(r"don't\(\)(?:.*?)", input_string)
    muls.extend(re.findall(r"mul\((?P<mul>\d*,\d*)", blocks.pop(0)))
    for block in blocks:
        if 'do()' in block:
            small_blocks = re.split(r"do\(\)(?:.*?)", block)
            sm_blocks = small_blocks[1::]
            for sm_block in sm_blocks:
                muls.extend(re.findall(r"mul\((?P<mul>\d*,\d*)\)", sm_block))
    return muls


def calc_result(muls: list) -> int:
    result = 0
    for pair in muls:
        val1, val2 = pair.split(',')
        result += int(val1) * int(val2)
    return result


if __name__ == '__main__':
    input_string = read_input()
    muls = find_muls(input_string)
    print(calc_result(muls))
