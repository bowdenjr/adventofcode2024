from scripts.utilities import open_advent_calendar


def all_increasing(report):

    for i in range(len(report) - 1):
        if report[i + 1] <= report[i]:
            return False

    return True


def all_decreasing(report):

    for i in range(len(report) - 1):
        if report[i + 1] >= report[i]:
            return False

    return True


def max_change(report):
    diffs = [abs(j - i) for i, j in zip(report[:-1], report[1:])]
    return max(diffs)


def dampen_report(report):

    dampened_reports = []

    for i, element in enumerate(report):
        report_copy = report.copy()
        report_copy.pop(i)
        dampened_reports.append(report_copy)

    return dampened_reports


def report_is_safe(report):

    if all_increasing(report):
        if max_change(report) <= 3:
            return True

    elif all_decreasing(report):
        if max_change(report) <= 3:
            return True

    return False


if __name__ == "__main__":

    # reports = open_advent_calendar("day_02\sample_input.txt")
    reports = open_advent_calendar("day_02\day_02_input.txt")
    reports = [report.split() for report in reports]
    reports = [[int(num) for num in report] for report in reports]

    part_1_count_of_safe = 0

    for report in reports:
        if report_is_safe(report):
            part_1_count_of_safe += 1
            continue

    print(f"Part 1 answer = {part_1_count_of_safe}")

    part_2_count_of_safe = 0
    for report in reports:
        if report_is_safe(report):
            part_2_count_of_safe += 1
            continue

        dampened_report_versions = dampen_report(report)

        for i, dampened_report in enumerate(dampened_report_versions):
            if report_is_safe(dampened_report):
                part_2_count_of_safe += 1
                break

    print(f"Part 2 answer = {part_2_count_of_safe}")
