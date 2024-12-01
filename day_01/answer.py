from scripts.utilities import (
    open_advent_calendar,
    abs_differences_between_two_lists,
    multiply_left_by_count_in_right,
)

# Part 1
lists = open_advent_calendar("day_01\sample_input.txt")
# lists = open_advent_calendar("day_01\day_01_input.txt")

left_list = [int(x.split()[0]) for x in lists]
right_list = [int(x.split()[-1]) for x in lists]
part_1_answer = abs_differences_between_two_lists(
                    left_list,right_list,sort=True)
print(sum(part_1_answer))

# Part 2
part_2_answer = multiply_left_by_count_in_right(left_list, right_list)
print(sum(part_2_answer))
