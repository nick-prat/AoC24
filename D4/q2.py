import sys

grid = [list(line.strip()) for line in sys.stdin]


def is_xmas(grid, x, y):
    if grid[x][y] != 'A':
        return False
    
    return ((grid[x-1][y-1] == 'M' and grid[x+1][y+1] == 'S') or (grid[x-1][y-1] == 'S' and grid[x+1][y+1] == 'M')) and ((grid[x-1][y+1] == 'M' and grid[x+1][y-1] == 'S') or (grid[x-1][y+1] == 'S' and grid[x+1][y-1] == 'M'))

sum = 0
for x in range(1, len(grid)-1):
    for y in range(1, len(grid[x])-1):
        sum += is_xmas(grid, x, y)
print(sum)
