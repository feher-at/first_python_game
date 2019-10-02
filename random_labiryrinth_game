import sys, termios, tty, os, time

ask_user = int(input("How big labirynt do you want to draw? :"))
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

button_delay = 0.01

def pseudo_random():
    import random
    
    map_size = ask_user
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

def search(x, y,grid):

    if grid[x][y] == 2:
        print("found")
        return True
    elif grid[x][y] == 1:
        return False
    elif grid[x][y] == 3:
        return False
    grid[x][y] = 3

    if ((x < len(grid)-1 and search(x+1, y,grid))

        or (y > 0 and search(x, y-1,grid))
        or (x > 0 and search(x-1, y,grid))
        or (y < len(grid)-1 and search(x, y+1,grid))):
        return True
    return False
def starting_player():
    while True:
        grid = pseudo_random()
        fy = 0
        fx = grid[0].index(0)

        if search(fy,fx,grid) == True:
            break

    grid[fy][fx] = 4
    return grid

def draw_game(map):
    
    for lists in map:
        for k in lists:
            if k == 2:
                print("Ü",end = "")
            elif k == 1:
                print("█",end = "")
            elif k ==0:
                print(" ",end="")
            elif k == 3:
                print(" ",end = "")
            elif k == 4:
                print("$",end = "")
        print()

            
def find_player(map):
    x = 0
    y = 0
    for map_line in range(len(map)):
        for line in range(len(map[map_line])):
            if map[map_line][line] == 4:
                x = line
                y = map_line
    return x,y
def win_coordinate(map):
    x= 0
    y= 0
    for map_line in range(len(map)):
        for line in range(len(map[map_line])):
            if map[map_line][line] == 2:
                x = line
                y = map_line
    return x,y

def check_valid_move(map, x, y, move):
    if move == "s":
        y += 1
    elif move == "w":
        y -= 1
    elif move == "a":
        x-=1
    elif move == "d":
        x+=1
    return map[y][x] == 0 or map[y][x] == 3 or map[y][x] == 4 or map[y][x] == 2

def modify_game(map,x,y,char):
    if char == "s":
        map[y][x] = 0
        y += 1
        map[y][x] = 4
    elif char == "w":
        map[y][x] = 0
        y -= 1
        map[y][x] = 4
    elif char == "a":
        map[y][x] = 0
        x-=1
        map[y][x] = 4
    elif char == "d":
        map[y][x] = 0
        x+=1
        map[y][x] = 4
def labirinth_game():
    grid = starting_player()
    
    while True:
        
        (x, y) = find_player(grid)
        (wx,wy) = win_coordinate(grid)
        os.system("clear")
        draw_game(grid)
        char = getch()
        if char == "q":
            exit()
        if wx == 0 and wy == 0:
            print("You won")
            break
        elif check_valid_move(grid, x, y, char):
            modify_game(grid, x, y,char)
            




labirinth_game()
