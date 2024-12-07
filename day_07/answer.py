from scripts.utilities import open_advent_calendar
from itertools import combinations, permutations, product, pairwise
from operator import mul, add
from copy import copy


def part1(equations):

    output = 0
    results = [eq.split(":")[0] for eq in equations]
    equations = [eq.split(":")[1] for eq in equations]
    equations = [eq.split() for eq in equations]
    number_groups = [[int(num) for num in eq] for eq in equations]

    for numbers, result in zip(number_groups, results):

        num_operators = len(numbers) - 1
        comb = list(product(["*", "+"], repeat=num_operators))
        possible_results = []

        for com in comb:

            partial_result = []

            for i, calc in enumerate(list(pairwise(numbers))):

                if len(com) == 1:
                    com = com[0]

                cal = list(copy(calc))
                if i == 0:
                    cal = [str(num) for num in cal]
                else:
                    cal = [partial_result, str(cal[1])]
                cal.insert(1, com[i])
                cal = "".join(cal)
                partial_result = str(eval(cal))

            possible_results.append(int(partial_result))

        if int(result) in possible_results:
            output += int(result)

    return output


def part2(equations):

    length = len(equations)
    output = 0
    results = [eq.split(":")[0] for eq in equations]
    equations = [eq.split(":")[1] for eq in equations]
    equations = [eq.split() for eq in equations]
    number_groups = [[int(num) for num in eq] for eq in equations]
    j = 0
    
    for numbers, result in zip(number_groups, results):
        
        j += 1
        print(f"at line {j} in {length} lines")
        num_operators = len(numbers) - 1
        comb = list(product(["*", "+", " "], repeat=num_operators))
        possible_results = []

        for com in comb:

            partial_result = []

            for i, calc in enumerate(list(pairwise(numbers))):

                if len(com) == 1:
                    com = com[0]

                cal = list(copy(calc))
                if i == 0:
                    cal = [str(num) for num in cal]
                else:
                    cal = [partial_result, str(cal[1])]
                cal.insert(1, com[i])
                cal = "".join(cal)
                if "*" in cal or "+" in cal:
                    partial_result = str(eval(cal))
                else:
                    partial_result = str(cal).replace(" ", "")

            possible_results.append(int(partial_result))

        if int(result) in possible_results:
            output += int(result)

    return output


if __name__ == "__main__":

    # equations = open_advent_calendar("day_07\sample_input_day_7.txt")
    equations = open_advent_calendar("day_07\day_07_input.txt")
    print(part2(equations))
