from scripts.utilities import open_advent_calendar
from itertools import repeat


def part1(disk):

    # Extrapolate
    compression = []
    id = 0
    i = 0
    j = 0

    while i < len(disk):

        size = int(disk[i])
        if i % 2 == 0: # file
            compression.append({"id": id, "size": size})
            id += 1
        else:  # free space
            compression.append({"space": size})
        i += 1

    dot_positions = []
    i = 0

    # Compress
    # Dot positions is a list of indices
    for item in compression:
        if len(item) == 2:
            i += item["size"]
        else:
            dot_positions.extend(list(range(i, i + item["space"])))
            i += item["space"]

    digits_list = [list(repeat(x["id"],x["size"])) for x in compression if "id" in x.keys()]
    digits = list(reversed([x for d in digits_list for x in d]))
    
    position = 0
    
    for item in range(len(dot_positions)): # stop when dot positions is at max
        if item % 2 == 0:
            compression[item] = list(repeat(compression[item]["id"], compression[item]["size"]))
        else:
            num_digits = compression[item]["space"]
            # check for end condition
            if dot_positions[position] > len(digits):
                compression = compression[:item]
                compression = [x for d in compression for x in d][:-dot_positions[position]+len(digits)]
                break
            compression[item] = digits[position:position+num_digits]
            position += num_digits

    # Update checksum
    checksum = 0
    for i, num in enumerate(compression):
        checksum += i * num

    return checksum


def part2(disk):

    # Extrapolate
    compression = []
    id = 0
    i = 0
    j = 0

    while i < len(disk):

        size = int(disk[i])
        if i % 2 == 0: # file
            compression.append({"id": id, "size": size})
            id += 1
        else:  # free space
            compression.append({"space": size})
        i += 1

    dot_positions = []
    i = 0

    # Compress
    # Dot positions is a list of indices
    for item in compression:
        if len(item) == 2:
            i += item["size"]
        else:
            dot_positions.extend(list(range(i, i + item["space"])))
            i += item["space"]

    digits_list = [list(repeat(x["id"],x["size"])) for x in compression if "id" in x.keys()]
    digits = list(reversed(digits_list))
    
    position = 0
    
    for item in range(len(dot_positions)): # stop when dot positions is at max
        if "id" in compression[item].keys():
            compression[item] = list(repeat(compression[item]["id"], compression[item]["size"]))
        else:
            # find the first block that fits:
            num_digits = compression[item]["space"]
            q = 0
            insertion = []
            while num_digits != 0 and q < len(digits): # stop when no more blocks to consider
                block = digits[q]                
                if len(block) <= num_digits:
                    insertion.extend(block)
                    num_digits -= len(block)
                    digits.remove(block)
                    try:
                        compression.remove({"id":block[0], "size": len(block)})
                    except KeyError:
                        pass
                q += 1
                        
            # check for end condition
            if dot_positions[position] > len(digits):
                compression = compression[:item]
                compression = [x for d in compression for x in d][:-dot_positions[position]+len(digits)]
                break
            compression[item] = insertion
            position += num_digits

    # Update checksum
    checksum = 0
    for i, num in enumerate(compression):
        checksum += i * num

    return checksum


if __name__ == "__main__":

    # disk = open_advent_calendar("day_09\day_09_input.txt")

    disk = ["2333133121414131402"]
    print(f"\nAnswer = {part2(*disk)}")

"""
00...111...2...333.44.5555.6666.777.888899

0099811188827773336446555566

0099811188827773336446555566..............

It is not
6390180901651 ? prob not
249097402995 too low
90994085674 too low
86357360908 too low

"""
