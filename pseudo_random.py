def pseudo_random():
    import random
    map_size = 10
    map = []
    first_random_list = [1,0]
    last_random_list = [1,2]
    first_lines = []
    ending_lines = []
    while len(first_lines) < map_size:
        first_lines.append(random.choice(first_random_list))
        for num in first_lines:
            if num == 0:
                while len(first_lines) < map_size:
                    first_lines.append(1)


    while len(ending_lines) < map_size:
        ending_lines.append(random.choice(last_random_list))
        for num in ending_lines:
            if num == 2:
                while len(ending_lines) < map_size:
                    ending_lines.append(1)
   
    

    between_line = []
    
    map.append(first_lines)
    while True:
        between_line.append(1)
        while True:
            between_line.append(random.randint(0,1))
            if len(between_line) == map_size-1:
                break
        between_line.append(1)
        map.append(between_line)
        between_line = []
        if len(map) == map_size-1:
            break
    map.append(ending_lines)

    return map
