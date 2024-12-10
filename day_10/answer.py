from scripts.utilities import open_advent_calendar


def find_next_digit(map, i, j, num):
    
    directions = [(0,1), (1,0), (0,-1), (-1,0)] # E, S, W, N
    for direction in directions:
        if map[i+direction[0]][j+direction[1]] == str(int(num)+1):
            yield([direction, num])
    return


def part1(map):
    
    part_1_answer = 0
    max_i = len(map[0])
    max_j = len(map)
    
    for i in range(max_i):
        for j in range(max_j):
            if map[i][j] == "0":
                path_length = [0,0]
                nextij = [0,0]
                next_digit = "0"
                cache = []
                while True:
                    next_directions = list(find_next_digit(map, i+path_length[0], j+path_length[1], next_digit))
                    cache.extend(next_directions)
                    if not cache:
                        break
                    if next_directions[0][1] == "9":
                        part_1_answer += 1
                        cache.pop(0)
                    else:
                        # keep exploring
                        nextij = cache[0][0]
                        path_length = [path_length[0] + nextij[0], path_length[1] + nextij[1]]
                        next_digit = map[i+path_length[0]][j+path_length[1]]
                        cache.pop(0)

                
                


def part2(map):
    pass



if __name__ == "__main__":

    # map = open_advent_calendar("day_10\day_10_input.txt")
    map = open_advent_calendar("day_10\sample_input_day_10.txt")

    # print(map)
    print(f"\nAnswer = {part1(map)}")
