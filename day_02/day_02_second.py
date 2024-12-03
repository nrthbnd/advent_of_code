from copy import deepcopy


def read_input() -> list[list[int]]:
    total_report = []
    with open('input.txt', 'r') as file:
        for line in file:
            total_report.append([int(value) for value in line.split(' ')])
    return total_report


def count_safe_reports(total_reports: list[list[int]]) -> int:
    safe_reports_count = 0
    for exact_report in total_reports:
        if check_report(exact_report):
            safe_reports_count += 1
        else:
            for i in range(len(exact_report)):
                report = deepcopy(exact_report)
                del report[i]
                if check_report(report):
                    safe_reports_count += 1
                    break
            continue
    return safe_reports_count


def check_report(checking_report: list[int]):
    report_values = range(len(checking_report) - 1)
    if all(abs(checking_report[i] - checking_report[i + 1]) in range(1, 4) for i in report_values) and \
            (all(checking_report[i] < checking_report[i + 1] for i in report_values) or
             all(checking_report[i] > checking_report[i + 1] for i in report_values)):
        return True
    else:
        return False


if __name__ == '__main__':
    values = read_input()
    safe_reports_count = count_safe_reports(values)
    print(safe_reports_count)
