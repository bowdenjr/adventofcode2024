from scripts.utilities import open_advent_calendar


def move(position, direction):
    if direction == 0: # north
        return position[0] - 1, position[1]
    elif direction == 1: #east
        return position[0], position[1] + 1
    elif direction == 2: #south:
        return position[0] + 1, position[1]
    elif direction == 3: # west
        return position[0], position[1] - 1

def step_back(position, direction):
    if direction == 0: # north
        return position[0] + 1, position[1]
    elif direction == 1: #east
        return position[0], position[1] - 1
    elif direction == 2: #south:
        return position[0] - 1, position[1]
    elif direction == 3: # west
        return position[0], position[1] + 1


def check_for_crossings(position, last_3_paths, direction):
    if direction == 0: # north
        return position[0] < last_3_paths[0][0][0] 
    elif direction == 1: #east
        return position[1] > last_3_paths[0][0][1]
    elif direction == 2: #south:
        return position[0] > last_3_paths[0][0][0]         
    elif direction == 3: # west
        return position[1] < last_3_paths[0][0][1]


def new_obstacle_creates_loop(maze, position, direction, visited_locations_and_dirs, side_locations_and_dirs):
    
    # Determine whether if I would to turn here would I end up on the existing path
    xmax = len(maze)
    ymax = len(maze[0])
    x, y = position[0], position[1]
    direction = (direction+1) % 4

    # search in the new direction for an exact existing path history
    while True:
        x, y = move(position, direction)

        if 0 > x or x >= xmax or 0 > y or y >= ymax:
            return False, side_locations_and_dirs
        elif maze[x][y] == "#":            
            direction = (direction+1) % 4
        elif (x, y, direction) in visited_locations_and_dirs.keys() or (x, y, direction) in side_locations_and_dirs.keys():
            return True, side_locations_and_dirs

        position = [x,y]
        side_locations_and_dirs[(x,y,direction)] = 1
    

def part1(initial_position, maze):

    position = initial_position
    xmax = len(maze)
    ymax = len(maze[0])
    visited_locations = {}
    direction = 0
    
    while True:
        x, y = move(position, direction)
        if 0 > x or x >= xmax or 0 > y or y > ymax:
            return sum(visited_locations.values())+1
        if maze[x][y] == "#":
            direction = (direction+1) % 4     
            continue
        position = [x,y]
        visited_locations[(x,y)] = 1
        


def new_obstacle_creates_loop_with_silly_exit(maze, position, direction, visited_locations_and_dirs):
    
    # Determine whether if I would to turn here would I end up on the existing path
    xmax = len(maze)
    ymax = len(maze[0])
    x, y = position[0], position[1]
    direction = (direction+1) % 4
    loop_counter = 0

    # search in the new direction for an exact existing path history
    while loop_counter < 99999:

        loop_counter += 1

        x, y = move(position, direction)

        if 0 > x or x >= xmax or 0 > y or y >= ymax:
            return False
        elif maze[x][y] == "#":            
            direction = (direction+1) % 4
        elif (x, y, direction) in visited_locations_and_dirs.keys():
            return True

        position = [x,y]
    
    return True


def part2(initial_position, maze):

    position = initial_position
    xmax = len(maze)
    ymax = len(maze[0])
    visited_locations_and_dirs = {(initial_position[0], initial_position[1], 0): 1}
    side_locations_and_dirs = {}
    direction = 0
    last_3_paths = []
    obstacle_count = 0
    last_obstacle = initial_position
    
    while True:
        
        x, y = move(position, direction)
        travel_distance = sum(visited_locations_and_dirs.values())+1
        print(f"I'm here: {position}, going {direction}, I've moved {travel_distance}")

        if 0 > x or x >= xmax or 0 > y or y > ymax:
            return obstacle_count
        
        if maze[x][y] == "#":
            direction = (direction+1) % 4
            print(f"OW!, OK I'm turning to {direction}")
            continue

        # loop, side_locations_and_dirs = new_obstacle_creates_loop(maze, [x,y], direction, visited_locations_and_dirs, side_locations_and_dirs)
        loop = new_obstacle_creates_loop_with_silly_exit(maze, [x,y], direction, visited_locations_and_dirs)
        
        if loop:
            print(f"You could put an obstacle to stop at {move([x,y],direction)}")
            obstacle_count += 1
            

        position = [x,y]
        visited_locations_and_dirs[(x,y,direction)] = 1



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
    print(f"Part 2 answer = {answer}") # 515 too low, 1908 too low, 4988 too high



"""
while True:
x, y = move(position, direction)
print(f"I'm here: {position}")

if 0 > x or x >= xmax or 0 > y or y > ymax:
    return obstacle_count

if maze[x][y] == "#":
    # if len(last_3_paths) == 3:
    #     last_3_paths.pop(0)
    # last_3_paths.append((last_obstacle, position))
    # last_obstacle = position
    direction = (direction+1) % 4
    print(f"OW!, OK I'm turning to {direction}")
    continue

# # Has the position path crossed the last 3 paths?
# if len(last_3_paths) == 3:
#     if check_for_crossings(position, last_3_paths, direction):
#         print(f"You could put an obstacle at {position}")
#         obstacle_count += 1

position = [x,y]        
visited_locations[(x,y)] = 1
    """