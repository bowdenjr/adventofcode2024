from scripts.utilities import (open_advent_calendar, report_is_safe,
                               dampen_report)


reports = open_advent_calendar("day_02\sample_input.txt")
# reports = open_advent_calendar("day_02\day_02_input.txt")
reports = [report.split() for report in reports]
reports = [[int(num) for num in report] for report in reports]

part_1_count_of_safe = sum(1 for report in reports 
                            if report_is_safe(report))

print(f"Part 1 answer = {part_1_count_of_safe}")

part_2_count_of_safe = 0

for report in reports:
    
    if report_is_safe(report):
        part_2_count_of_safe += 1
        continue
    
    if any(report_is_safe(report) for report in dampen_report(report)):
        part_2_count_of_safe += 1
            
print(f"Part 2 answer = {part_2_count_of_safe}")
