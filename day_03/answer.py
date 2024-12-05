import re
from itertools import chain
from scripts.utilities import open_advent_calendar


def part1(input_data: str) -> None:

    calculations = re.findall("mul\(\d*,\d*\)", input_data)
    calculations = "".join(calculations)
    calculations = re.findall("\d*,\d*", calculations)
    calculations = [x.split(",") for x in calculations]
    calculations = [int(x[0]) * int(x[1]) for x in calculations]
    print(sum(calculations))


def part2(input_data: str) -> None:

    instructions = re.sub("don't\(\).*?do\(\)", "", data)
    part1(instructions)


if __name__ == "__main__":

    # data = open_advent_calendar("day_03\sample_input_day_03.txt")
    # data = open_advent_calendar("day_03\sample_input_day_03_part2.txt")
    data = open_advent_calendar(r"day_03\day_03_input.txt")
    data = [line.split("\n")[0] for line in data]
    data = "".join(data)
    part2(data)
