from scripts.utilities import open_advent_calendar


def part1(grid):
    
    part1answer = 0
    # Make 4x4 grids
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == len(grid) - 3:
                subgrid = [grid[i][j:j+4],grid[i+1][j:j+4],grid[i+2][j:j+4]]
            elif i == len(grid) - 2:
                subgrid = [grid[i][j:j+4],grid[i+1][j:j+4]]
            elif i == len(grid) - 1:
                subgrid = [grid[i][j:j+4]]
            elif j == len(grid[i]) - 3:
                subgrid = [grid[i][j:j+3],grid[i+1][j:j+3],grid[i+2][j:j+3],grid[i+3][j:j+3]]
            elif j == len(grid[i]) - 2:
                subgrid = [grid[i][j:j+2],grid[i+1][j:j+2],grid[i+2][j:j+2],grid[i+3][j:j+2]]
            elif j == len(grid[i]) - 1:
                subgrid = [grid[i][j:j+1],grid[i+1][j:j+1],grid[i+2][j:j+1],grid[i+3][j:j+1]]
            else:
                subgrid = [grid[i][j:j+4],grid[i+1][j:j+4],grid[i+2][j:j+4],grid[i+3][j:j+4]]
            
            # MISSING AN UP/DOWN, they should be at i=4, i=3OK and i = 9
            
                        
            if all([len(x)==4 for x in subgrid]):
                # Check top row for word left or right
                if "XMAS" in subgrid[0] or "SAMX" in subgrid[0]:
                    part1answer += 1
            
            if len(subgrid) == 4:
                # Check for vertical down
                if subgrid[0][0] == "X" and subgrid[1][0] == "M" and subgrid[2][0] == "A" and subgrid[3][0] == "S":
                    part1answer += 1
                    print("UP/DOWN FOUND")
                                        
                # Check for vertical up
                if subgrid[0][0] == "S" and subgrid[1][0] == "A" and subgrid[2][0] == "M" and subgrid[3][0] == "X":
                    part1answer += 1         
                    print("UP/DOWN FOUND")   
            
            if len(subgrid) == 4 and all([len(x)==4 for x in subgrid]):
                # Check for diag down right
                if subgrid[0][0] == "X" and subgrid[1][1] == "M" and subgrid[2][2] == "A" and subgrid[3][3] == "S":
                    part1answer += 1
                    print("DIAG DOWN RIGHT FOUND")
                # Check for diag up left
                if subgrid[3][3] == "X" and subgrid[2][2] == "M" and subgrid[1][1] == "A" and subgrid[0][0] == "S":
                    part1answer += 1
                    print("DIAG UP LEFT FOUND")
                # Check for diag up right
                if subgrid[3][0] == "X" and subgrid[2][1] == "M" and subgrid[1][2] == "A" and subgrid[0][3] == "S":
                    part1answer += 1
                    print("DIAG UP RIGHT FOUND")
                # Check for diag down left
                if subgrid[0][3] == "X" and subgrid[1][2] == "M" and subgrid[2][1] == "A" and subgrid[3][0] == "S":
                    part1answer += 1
                    print("DIAG DOWN LEFT FOUND")
            
    print(part1answer)
    

def part2(grid):
    
    part2answer = 0
    # Make 3x3 grids
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i < (len(grid)-2) and j < (len(grid[0])-2):
                subgrid = [grid[i][j:j+3],grid[i+1][j:j+3],grid[i+2][j:j+3]]
        
                # Start at 00 and 02
                if subgrid[0][0] == "M" and subgrid[1][1] == "A" and subgrid[2][2] == "S" and subgrid[0][2] == "M" and subgrid[1][1] == "A" and subgrid[2][0] == "S":
                    part2answer += 1
                    print(f"X found at {(i,j)}")
                
                # Start at 00 and 20
                if subgrid[0][0] == "M" and subgrid[1][1] == "A" and subgrid[2][2] == "S" and subgrid[2][0] == "M" and subgrid[1][1] == "A" and subgrid[0][2] == "S":
                    part2answer += 1
                    print(f"X found at {(i,j)}")
                
                # Start at 02 and 22
                if subgrid[0][2] == "M" and subgrid[1][1] == "A" and subgrid[2][0] == "S" and subgrid[2][2] == "M" and subgrid[1][1] == "A" and subgrid[0][0] == "S":
                    part2answer += 1
                    print(f"X found at {(i,j)}")
                    
                # Start at 20 and 22
                if subgrid[2][2] == "M" and subgrid[1][1] == "A" and subgrid[0][0] == "S" and subgrid[2][0] == "M" and subgrid[1][1] == "A" and subgrid[0][2] == "S":
                    part2answer += 1
                    print(f"X found at {(i,j)}")
                    


                
    print(part2answer)
    

if __name__ == '__main__':

    # grid = open_advent_calendar("day_04\sample_input_day_04.txt")
    grid = open_advent_calendar("day_04\day_04_input.txt")
    part2(grid)
    