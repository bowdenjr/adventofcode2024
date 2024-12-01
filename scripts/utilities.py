from typing import List, Union


def open_advent_calendar(path) -> List[str]:
    with open(path, "r") as f:
        return f.read().split("\n")


def abs_differences_between_two_lists(
    left_list: List[Union[float, int]],
    right_list: List[Union[float, int]],
    sort: bool) -> List[Union[float, int]]:

    if len(left_list) != len(right_list):
        raise IndexError("Lists are of different lengths")

    if sort:
        left_list = sorted(left_list)
        right_list = sorted(right_list)
        return [abs(right_list[num] - left_list[num])
                for num in range(len(left_list))]
    else:
        return [abs(right_list[num] - left_list[num])
                for num in range(len(left_list))]


def multiply_left_by_count_in_right(
    left_list: List[Union[float, int]],
    right_list: List[Union[float, int]]
):
    return [num * right_list.count(num) for num in left_list]
