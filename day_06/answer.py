from scripts.utilities import open_advent_calendar
from copy import copy


def move(position, direction):
    if direction == 0: # north
        return position[0] - 1, position[1]
    elif direction == 1: #east
        return position[0], position[1] + 1
    elif direction == 2: #south:
        return position[0] + 1, position[1]
    elif direction == 3: # west
        return position[0], position[1] - 1


def part1(initial_position, maze):

    position = initial_position
    xmax = len(maze)
    ymax = len(maze[0])
    visited_locations = {}
    direction = 0

    while True:
        x, y = move(position, direction)
        if 0 > x or x >= xmax or 0 > y or y > ymax:
            return sum(visited_locations.values())+1, visited_locations
        if maze[x][y] == "#":
            direction = (direction+1) % 4     
            continue
        position = [x,y]
        visited_locations[(x,y)] = 1


def loop(maze, position, direction):

    xmax = len(maze)
    ymax = len(maze[0])
    x, y = position[0], position[1]
    visited_locations_and_dirs = set()

    while True:
        x, y = move(position, direction)

        if (x, y, direction) in visited_locations_and_dirs:
            return True
        if 0 > x or x >= xmax or 0 > y or y >= ymax:
            return False
        if maze[x][y] == "#":            
            direction = (direction+1) % 4            
        else:
            position = [x,y]
            visited_locations_and_dirs.add((x,y,direction))


def part2(initial_position, maze):

    xmax = len(maze)
    ymax = len(maze[0])
    obstacle_count = 0

    for x in range(xmax):
        for y in range(ymax):
            
            print(f"Scanning {(x, y)} out of {(xmax, ymax)}")
            
            if maze[x][y] == "#" or (x, y) == initial_position:
                continue
            
            new = list(maze[x])
            new[y] = "#"
            maze[x] = "".join(new)
            
            obstacle_count += loop(maze, initial_position, 0)
            
            new = list(maze[x])
            new[y] = "."
            maze[x] = "".join(new)
    
    return obstacle_count

"""
Obstacles should be at [6,3], [7,6], [8,1], [8,3], [7, 7], [9,7]
"""


if __name__ == '__main__':
    
    maze = open_advent_calendar("day_06\day_06_input.txt")    
    # maze = open_advent_calendar("day_06\sample_input_day_06.txt")    
    initial_position = [[x, y.find("^")] for x, y in enumerate(maze) if y.find("^") > 0]
    # answer = part1(*initial_position, maze)            
    # print(f"Part 1 answer = {answer}")
    answer = part2(*initial_position, maze)
    print(f"Part 2 answer = {answer}") 
    
# 515 and 1908 too low, 3811 and 4988 too high, 2238 not right, 1946 not right, 1945 not right
