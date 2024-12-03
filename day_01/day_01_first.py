

def read_input() -> tuple[list, list]:
    first_list = []
    second_list = []
    with open('input.txt', 'r') as file:
        for line in file:
            values = line.split(' ')
            first, second = values[0], values[-1]
            first_list.append(int(first))
            second_list.append(int(second))

    return first_list, second_list


def count_distances(first_list: list, second_list:list) -> int:
    first_list = sorted(first_list)
    second_list = sorted(second_list)
    total_distance = 0
    for _ in range(len(first_list)):
        first_val, second_val = first_list.pop(0), second_list.pop(0)
        total_distance += abs(second_val - first_val)
    return total_distance


if __name__ == '__main__':
    values = read_input()
    total_distance = count_distances(*values)
    print(total_distance)
