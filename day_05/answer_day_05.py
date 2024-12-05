from scripts.utilities import open_advent_calendar
from collections import deque


def part1(rules, updates):

    output = 0

    for update in updates:
        valid = True
        updates_map = {k: i for i, k in enumerate(update)}
        for a, b in rules:
            if a not in updates_map.keys() or b not in updates_map.keys():
                continue
            if updates_map[a] > updates_map[b]:
                valid = False
                break
        if valid:
            output += int(update[len(update) // 2])

    print(output)


def part2(rules, updates):

    output = 0

    for update in updates:

        valid = True
        updates_map = {k: i for i, k in enumerate(update)}
        for a, b in rules:
            if a not in updates_map.keys() or b not in updates_map.keys():
                continue
            if updates_map[a] > updates_map[b]:
                valid = False
                break
        if valid:
            continue

        # Kahn's Algorithm
        adjacencies = {k: [] for k in update}

        for a, b in rules:
            if a not in update or b not in update:
                continue
            adjacencies[a].append(b)

        indegrees = {k: 0 for k in update}

        for key in adjacencies:
            indegrees[key] = len(adjacencies[key])

        q = deque()
        q.append(*[k for k, v in indegrees.items() if v == 0])

        sorted_update = []

        while True:
            current = q.pop()
            indegrees.pop(current)
            sorted_update.insert(0, current)

            if len(sorted_update) == len(update):
                break

            for adjacency, value in adjacencies.items():
                if current in adjacencies[adjacency]:
                    indegrees[adjacency] -= 1
                zero_indegrees = [k for k, v in indegrees.items() if v == 0]
                if zero_indegrees:
                    q.append(*zero_indegrees)
            if len(q) == 0:
                break

        output += int(sorted_update[len(sorted_update) // 2])

    print(output)


if __name__ == "__main__":

    # data = open_advent_calendar("day_05\sample_input_day_05.txt")
    data = open_advent_calendar("day_05\day_05_input.txt")
    rules = data[: data.index("")]
    updates = data[data.index("") + 1 :]
    updates = [update.split(",") for update in updates]
    rules = [(x.split("|")[0], x.split("|")[1]) for x in rules]

    part2(rules, updates)
