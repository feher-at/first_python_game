from pseudo_random_labirinth import pseudo_random

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
