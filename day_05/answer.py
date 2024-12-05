from scripts.utilities import open_advent_calendar


def part1(rules, updates):
    
    main = []

    for a, b in rules:        
        if a not in main:
            main.insert(0, a)
        if b not in main:
            main.insert(0, b)
    
    not_sorted = True
    while not_sorted:
        for page in main:            
            for a, b in rules:              
                if page == a:
                    if main.index(page) > main.index(b):
                        main.insert(main.index(b), main.pop(main.index(page)))
                        not_sorted = True
                if page == b:
                    if main.index(page) < main.index(a):
                        main.insert(main.index(page), main.pop(main.index(a)))
                        not_sorted = True
                    

        not_sorted = False

    part1answer = 0
    
    # Check each update for right order
    for update in updates:
        order_for_checking = [main.index(page) for page in update]
        if sorted(order_for_checking) == order_for_checking:
            part1answer += int(update[len(update) // 2])
        
    
    # Find the middle number

    print(part1answer) # 252 too low


if __name__ == '__main__':

    data = open_advent_calendar("day_05\sample_input_day_05.txt")
    # data = open_advent_calendar("day_05\day_05_input.txt")
    rules = data[:data.index("")]
    updates = data[data.index("")+1:]
    updates = [update.split(",") for update in updates]
    rules = [(x.split("|")[0],x.split("|")[1]) for x in rules]
    
    part1(rules, updates) 
    