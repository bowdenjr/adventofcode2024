from scripts.utilities import open_advent_calendar
from collections import defaultdict


def blink(stones):
    
    new_stones = defaultdict(int)
    
    for stone in stones:
        if stone == 0:
            new_stones[1] += stones[stone]
        elif len(str(stone)) % 2 == 0:
            str_length = len(str(stone)) // 2
            left = int(str(stone)[:str_length])
            right = int(str(stone)[str_length:])
            new_stones[left] += stones[stone]
            new_stones[right] += stones[stone] 
        else:
            new_stones[stone * 2024] += stones[stone]
 
    return new_stones


def part1and2(input_stones):
    
    i = 0
    MAX_ITER = 75
    stones = defaultdict(int)
    
    input_stones = [int(stone) for stone in input_stones]
    
    for stone in input_stones:
        stones[stone] += 1
    
    while i < MAX_ITER:
        i += 1
        new_stones = blink(stones)
        stones = new_stones
        
    return sum(stones.values())
    
            
if __name__ == "__main__":

    # input_stones = "125 17".split()
    input_stones = open_advent_calendar("day_11\day_11_input.txt")[0].split()

    # print(map)
    print(f"\nAnswer = {part1and2(input_stones)}")
