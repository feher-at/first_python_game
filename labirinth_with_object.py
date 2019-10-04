import sys, termios, tty, os, time
from maze_maps import maps
import random
import pygame


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

QUESTIONS = [["Minek megy a vak az erdőbe","fának"],
             ["Hogy hívják a legmelegebb hálózatot","katlan"],
             ["Hol terem a CD ROM","diszkréten"],
             ["Mit mond az orosz pap a halálos ágyán","szentpétervár"],
             ["Mi lesz ha elütnek egy matematikust","már nem számít"],
             ["Mi a női programozók rémálma","végtelen ciklus"],
             ["Hogy hívják a templomok közötti hálózatot","paplan"]]

def draw_game(map):
    
    for lists in map:
        
        for k in lists:
            if k == 2:
                print("$",end = "")
            elif k == 1:
                print("█",end = "")
            elif k ==0:
                print(" ",end = "")
            elif k == 3:
                print("Ű",end = "")
            elif k == 4:
                print("¤",end = "")
            elif k == "?":
                print("?",end = "")
        print()
            
def find_player(map):
    x = 0
    y = 0
    for map_line in range(len(map)):
        for line in range(len(map[map_line])):
            if map[map_line][line] == 2:
                x = line
                y = map_line
    return x,y

def objectums(map):
    all_object_on_the_map = 0
    for map_line in range(len(map)):
        for line in range(len(map[map_line])):
            if map[map_line][line] == 4:
                all_object_on_the_map += 1
    return all_object_on_the_map

def questions(map):
    questions_coordinate = []
    for map_line in range(len(map)):
        for line in range(len(map[map_line])):
            if map[map_line][line] == "?":
                questions_coordinate.append([map_line,line])                
    return questions_coordinate

def win_coordinate(map):
    x= 0
    y= 0
    for map_line in range(len(map)):
        for line in range(len(map[map_line])):
            if map[map_line][line] == 3:
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
    return map[y][x] == 0 or map[y][x] == 3 or map[y][x] == 4 or map[y][x] == "?"

def modify_game(map,x,y,char):
    if char == "s":
        map[y][x] = 0
        y += 1
        map[y][x] = 2
    elif char == "w":
        map[y][x] = 0
        y -= 1
        map[y][x] = 2
    elif char == "a":
        map[y][x] = 0
        x-=1
        map[y][x] = 2
    elif char == "d":
        map[y][x] = 0
        x+=1
        map[y][x] = 2
def music():
    step = "labirinth_song.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(step)
    pygame.mixer.music.play()
def labirinth_game():
    step = "labirinth_song.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(step)
    pygame.mixer.music.play(-1)
    
    
    for the_map in maps():
        questions_coordinates = questions(the_map)
        (wx,wy) = win_coordinate(the_map)

        while True: 
            [x, y] = find_player(the_map)
            objectums_number = objectums(the_map)
            os.system("clear")
            draw_game(the_map)
            if [y,x] in questions_coordinates:
                the_question = random.choice(QUESTIONS)
                while True:
                    question = input(the_question[0] + "?  ")
                    if question != the_question[1]:
                        print("False!")
                    else:
                        print("True!")
                        QUESTIONS.remove(the_question)
                        break
                questions_coordinates.pop(questions_coordinates.index([y,x]))
            char = getch()
            if char == "q":
                exit()
            if objectums_number == 0 and len(questions_coordinates) == 0:
                the_map[wy-1][wx] = 0

            if wx == x and wy == y:
                print("You won")
                break
            
            elif check_valid_move(the_map, x, y, char):
                modify_game(the_map, x, y,char)



labirinth_game()
