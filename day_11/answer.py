from scripts.utilities import open_advent_calendar
import math


def compute_new_stones(stone):
    
    if stone == 0:
        return 1
    elif int(math.log10(stone)+1) % 2 == 0:
        dec = 10**int((math.log10(stone)+1)//2)
        dec_split = stone / dec
        left = compute_new_stones(int(dec_split))
        right = compute_new_stones(int(round(dec * (dec_split - int(dec_split)), int((math.log10(stone) + 1) // 2))))
        return [left, right]
    else:
        return stone * 2024
    

def part1(stones):

    blinks = 25
    
    stones = [int(stone) for stone in stones]

    for blink in range(blinks):        
        
        new_stones = []
        print(f"At blink: {blink}")

        for stone in stones:
            
            new_stones.append(compute_new_stones(stone))

            # if stone == 0:
            #     new_stones.append(1)
            # elif int(math.log10(stone)+1) % 2 == 0:
            #     dec = 10**int((math.log10(stone)+1)//2)
            #     dec_split = stone / dec
            #     new_stones.extend([int(dec_split), int(round(dec*(dec_split - int(dec_split)),int((math.log10(stone)+1)//2)))])
            # else:
            #     new_stones.append(stone * 2024)
                
        stones = new_stones

    return len(stones)
            
            
if __name__ == "__main__":

    stones  = "125 17".split()
    # stones = open_advent_calendar("day_11\day_11_input.txt")[0].split()

    # print(map)
    print(f"\nAnswer = {part1(stones)}")
    # compute_new_stones()