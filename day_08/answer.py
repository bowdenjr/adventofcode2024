from scripts.utilities import open_advent_calendar
import itertools
from copy import copy


def get_antenna_locations(grid, antenna: str) -> list:
    # Find all antennas of inputted antenna
    locations = []
    for i, row in enumerate(grid):
        if any([col == antenna for col in row]):
            locations.extend([(i, j) for j, char in enumerate(row) if char == antenna])
    return locations


def get_points(loc, direction, maxrow, maxcol):
    """
    directions:
    0 = NE dec r, inc c
    1 = SE inc r, inc c
    2 = SW inc r, dec c
    3 = NW dec c, dec r
    """
    points = []
    tranlsations = itertools.product(list(range(1, maxrow)), repeat=2)

    if direction == 0:
        for translation in tranlsations:
            local_points = []
            last_point = loc
            while True:
                if (
                    last_point[0] - translation[0] < 0
                    or last_point[1] + translation[1] >= maxcol
                ):
                    break
                local_points.append(
                    (last_point[0] - translation[0], last_point[1] + translation[1])
                )
                last_point = (
                    last_point[0] - translation[0],
                    last_point[1] + translation[1],
                )
            points.append(local_points) if len(local_points) > 1 else None

    elif direction == 1:
        for translation in tranlsations:
            local_points = []
            last_point = loc
            while True:
                if (
                    last_point[0] + translation[0] >= maxrow
                    or last_point[1] + translation[1] >= maxcol
                ):
                    break
                local_points.append(
                    (last_point[0] + translation[0], last_point[1] + translation[1])
                )
                last_point = (
                    last_point[0] + translation[0],
                    last_point[1] + translation[1],
                )
            points.append(local_points) if len(local_points) > 1 else None

    elif direction == 2:
        for translation in tranlsations:
            local_points = []
            last_point = loc
            while True:
                if (
                    last_point[0] + translation[0] >= maxrow
                    or last_point[1] - translation[1] < 0
                ):
                    break
                local_points.append(
                    (last_point[0] + translation[0], last_point[1] - translation[1])
                )
                last_point = (
                    last_point[0] + translation[0],
                    last_point[1] - translation[1],
                )
            points.append(local_points) if len(local_points) > 1 else None

    elif direction == 3:
        for translation in tranlsations:
            local_points = []
            last_point = loc
            while True:
                if (
                    last_point[0] - translation[0] < 0
                    or last_point[1] - translation[1] < 0
                ):
                    break
                local_points.append(
                    (last_point[0] - translation[0], last_point[1] - translation[1])
                )
                last_point = (
                    last_point[0] - translation[0],
                    last_point[1] - translation[1],
                )
            points.append(local_points) if len(local_points) > 1 else None

    return points


def part1(grid):

    antennas = set("".join(grid))
    antennas.remove(".")
    maxrow = len(grid[0])
    maxcol = len(grid)
    antinode_locations = []

    num_ans = 0
    node_grid = copy(grid)

    for antenna in sorted(antennas):

        locations = get_antenna_locations(grid, antenna)

        for location in locations:

            paths = []

            for direction in range(4):
                paths.extend(get_points(location, direction, maxrow, maxcol))

            other_locations = [
                other_loc for other_loc in locations if other_loc != location
            ]

            for other_location in other_locations:

                antinode_locations = []

                for path in paths:

                    if other_location in path and path.index(other_location) != (
                        len(path)
                    ):

                        antinode_locations.append(path[path.index(other_location) + 1])

                        # if an

                        for an in antinode_locations:
                            if node_grid[an[0]][an[1]] == ".":
                                node_grid[an[0]] = (
                                    node_grid[an[0]][: an[1]]
                                    + "#"
                                    + node_grid[an[0]][an[1]]
                                )

    for i in range(maxrow):
        for j in range(maxcol):
            if node_grid[i][j] != ".":
                num_ans += 1


def part2(grid):

    antennas = set("".join(grid))
    antennas.remove(".")
    maxrow = len(grid[0])
    maxcol = len(grid)
    antinode_locations = []

    num_ans = 0
    node_grid = copy(grid)

    for antenna in sorted(antennas):

        locations = get_antenna_locations(grid, antenna)

        for location in locations:

            paths = []

            for direction in range(4):
                paths.extend(get_points(location, direction, maxrow, maxcol))

            other_locations = [
                other_loc for other_loc in locations if other_loc != location
            ]

            for other_location in other_locations:

                antinode_locations = []

                for path in paths:

                    if other_location in path and path.index(other_location) != (
                        len(path) - 1
                    ):

                        antinode_locations.extend(
                            path[path.index(other_location) + 1 :]
                        )

                        for an in antinode_locations:
                            if node_grid[an[0]][an[1]] == ".":
                                node_grid[an[0]] = (
                                    node_grid[an[0]][: an[1]]
                                    + "#"
                                    + node_grid[an[0]][an[1] + 1 :]
                                )

    for i in range(maxrow):
        for j in range(maxcol):
            if node_grid[i][j] != ".":
                num_ans += 1

    print(f"Answer = {num_ans}")


if __name__ == "__main__":

    # grid = open_advent_calendar("day_08\sample_input_day_08.txt")
    grid = open_advent_calendar("day_08\day_08_input.txt")
    # part1(grid) # I broke it
    part2(grid)
