from scripts.utilities import open_advent_calendar
from itertools import repeat
from time import perf_counter
import re

def part1(disk):

    # Extrapolate
    compression = ""
    id = 0
    i = 0
    j = 0

    while i < len(disk):
        
        size = int(disk[i])
        if i % 2 == 0: # file
            file = "".join([str(x) for x in list(repeat(id, size))])
            compression += file
            id += 1
            j += len(file)
        else: # free space
            space = "".join(list(repeat(".",size)))
            compression += space
            j += len(space)
        i += 1

    # Compress
    i = len(compression)
    compression_list = list(compression)
    dot_positions = [i for i, x in enumerate(compression_list) if x == "."]
    digits = list(reversed([x for x in compression_list if x.isdigit()]))
    
    for dot_position, digit in zip(dot_positions, digits):
        compression_list[dot_position] = digit

    compression_list = compression_list[:-len(dot_positions)]

    # Update checksum
    checksum = 0
    for i, char in enumerate(compression_list):
        checksum += i * int(char)

    print("".join(compression_list))
    return checksum

if __name__ == "__main__":

    disk = open_advent_calendar("day_09\day_09_input.txt")
    # disk = open_advent_calendar("day_09\sample_input_day_09.txt")
    print(f"Answer = {part1(*disk)}") # 90994085674 too low

"""
0099811188827773336446555566
0099811188827773336446555566..............
"""