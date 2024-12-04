import sys

grid = [list(line.strip()) for line in sys.stdin]

def is_xmas_dir(grid, x, y, dir):
    dx = dir[0]
    dy = dir[1]

    if dx < 0 and x < 3:
        return False
    
    if dx > 0 and x >= len(grid[y]) - 3:
        return False

    if dy < 0 and y < 3:
        return False
    
    if dy > 0 and y >= len(grid) - 3:
        return False
    
    k = ['M', 'A', 'S']
    for d in range(1,4):
        if grid[x + d * dx][y + d * dy] != k[d-1]:
            # print('failed ', x, y, dx, dy, x + d * dx, y + d * dy, grid[x + d * dx][y + d * dy], k[d-1], dir)
            return False
    
    return True


DIRS = [
    [0,-1],[0,1],
    [1,-1],[1,0],[1,1],
    [-1,-1],[-1,0],[-1,1],
]
    

def is_xmas(grid, x, y):
    if grid[x][y] != 'X':
        return False
    
    global DIRS

    sum = 0
    for dir in DIRS:
        if is_xmas_dir(grid, x, y, dir):
            sum += 1
    return sum
    
sum = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        sum += is_xmas(grid, x, y)
print(sum)
