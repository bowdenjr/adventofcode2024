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
        
        
def part2(initial_position, maze):

    position = initial_position
    xmax = len(maze)
    ymax = len(maze[0])
    visited_locations = {}
    direction = 0
    last_3_paths = []
    obstacle_count = 0
    last_obstacle = initial_position
    
    while True:
        x, y = move(position, direction)
        if 0 > x or x >= xmax or 0 > y or y > ymax:
            return obstacle_count
        if maze[x][y] == "#":
            if len(last_3_paths) == 3:
                last_3_paths.pop(0)
            last_3_paths.append((last_obstacle, position))
            last_obstacle = position
            direction = (direction+1) % 4
            continue
        # Has the position path crossed the last 3 paths?
        if len(last_3_paths) == 3:
            if check_for_crossings(position, last_3_paths, direction):
                obstacle_count += 1
    

        position = [x,y]
        
        visited_locations[(x,y)] = 1
    
    return obstacle_count





if __name__ == '__main__':
    
    # maze = open_advent_calendar("day_06\day_06_input.txt")    
    maze = open_advent_calendar("day_06\sample_input_day_06.txt")    
    initial_position = [[x, y.find("^")] for x, y in enumerate(maze) if y.find("^") > 0]
    # answer = part1(*initial_position, maze)            
    # print(f"Part 1 answer = {answer}")
    answer = part2(*initial_position, maze)
    print(f"Part 2 answer = {answer}")