from scripts.utilities import open_advent_calendar


def is_connected(map, node, maxi, maxj):

    connected_dirs = []
    char = map[node[0]][node[1]]
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    for direction in directions:        
        if 0 <= (node[0] + direction[0]) < maxi and 0 <= (node[1] + direction[1]) < maxj:
            if map[node[0] + direction[0]][node[1] + direction[1]] == char:
                connected_dirs.append(direction)
    return connected_dirs


def part1(map):

    maxi = len(map[0])
    maxj = len(map)

    visited = []
    fences = 0    
    
    for i in range(maxi):
        for j in range(maxj):
            if (i,j) not in visited:
                visited.append((i,j))
                connections = is_connected(map, [i,j], maxi, maxj)
                if connections:
                    # deteremine type of node:
                    edge = (i in [i,maxi] or j in [j, maxj])

                    if not edge:
                        if len(connections) == 3:
                            fences += 1
                        elif len(connections) == 2:
                            fences += 2
                        elif len(connections) == 1:
                            fences += 3

                    else: # edge cases
                        if len(connections) == 3:
                            fences += 1
                        elif len(connections) == 2:
                            fences += 2 # I think
                        elif len(connections) == 1:
                            fences += 3
                        elif len(connections) == 0:
                            fences += 4

            print(f"Node {(i,j)} is connected in {len(connections)} places, so fences are now at: {fences}")

    return fences
                        

if __name__ == "__main__":
    
    map = open_advent_calendar("day_12\sample_input_day_12.txt")
    part1answer = part1(map)
    print(f"Part 1 Answer = {part1answer}")
