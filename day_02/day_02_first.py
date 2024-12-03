

def read_input() -> list[list[int]]:
    total_report = []
    with open('input.txt', 'r') as file:
        for line in file:
            total_report.append([int(value) for value in line.split(' ')])
    return total_report


def count_safe_reports(total_reports: list[list[int]]) -> int:
    safe_reports_count = 0
    for exact_report in total_reports:
        report_values = range(len(exact_report) - 1)
        if all(abs(exact_report[i] - exact_report[i + 1]) in range(1, 4) for i in report_values) and \
                (all(exact_report[i] < exact_report[i + 1] for i in report_values) or
                 all(exact_report[i] > exact_report[i + 1] for i in report_values)):
            safe_reports_count += 1
        else:
            continue
    return safe_reports_count


if __name__ == '__main__':
    values = read_input()
    safe_reports_count = count_safe_reports(values)
    print(safe_reports_count)
