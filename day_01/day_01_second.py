

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


def count_similarity(first_list: list, second_list:list) -> int:
    appearing_dict = {}
    similarity_score = 0
    for value in first_list:
        if value not in appearing_dict:
            appearing_count = second_list.count(value)
            appearing_dict[value] = appearing_count
        similarity_score += appearing_dict[value]  * value

    return similarity_score


if __name__ == '__main__':
    values = read_input()
    similarity_score = count_similarity(*values)
    print(similarity_score)
