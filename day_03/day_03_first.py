import re


def read_input() -> str:
    with open('input_1.txt', 'r') as file:
        input_string = file.read()
    return input_string


def find_muls(input_string: str) -> list:
    pattern = r'mul\((?P<mul_value>\d*,\d*)\)'
    return [pair.split(',') for pair in re.findall(pattern, input_string)]


def calc_result(muls: list) -> int:
    result = 0
    for pair in muls:
        result += int(pair[0]) * int(pair[-1])
    return result


if __name__ == '__main__':
    input_string = read_input()
    muls = find_muls(input_string)
    print(calc_result(muls))
