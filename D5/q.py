import sys
import time
import copy

grid = [[c for c in line.strip()] for line in sys.stdin]

l = None
for r in range(len(grid)):
  for c in range(len(grid[r])):
    if grid[r][c] in ['^', '>', 'v', '<']:
      l = (r,c)
      if grid[r][c] == '^':
        d = (-1,0)
      elif grid[r][c] == '>':
        d = (0,1)
      elif grid[r][c] == 'v':
        d = (-1,0)
      elif grid[r][c] == '>':
        d = (-1,0)

def rotate(d):
  return (d[1], -d[0])

def print_g(g, v):
  s = set()
  for i in v:
    s.update(v[i])
  for rg in range(len(g)):
    for cg in range(len(g[rg])):
      if (rg, cg) in s:
        print('X', end='')
      else:
        print(g[rg][cg], end='')
    print('')
  print('')
  time.sleep(0.25)


def is_out_of_bounds(g, l):
  return l[0] < 0 or l[1] < 0 or l[0] >= len(g) or l[1] >= len(g[l[0]])


def will_loop(g, l, d, v):
  while True:
    if l in v[d]:
      return True

    v[d].add(l)

    nl = (l[0] + d[0], l[1] + d[1])

    if is_out_of_bounds(g, nl):
      return False
    
    if g[nl[0]][nl[1]] == '#':
      d = rotate(d)
    else:
      l = nl

v = {
  (0,1): set(),
  (1,0): set(),
  (0,-1): set(),
  (-1,0): set()
}

found_loops = set()

while True:
  v[d].add(l)
  nl = (l[0] + d[0], l[1] + d[1])
  
  if is_out_of_bounds(grid, nl):
    break
  elif grid[nl[0]][nl[1]] == '#':
    d = rotate(d)
    continue
  elif grid[nl[0]][nl[1]] == '.':
    grid[nl[0]][nl[1]] = '#'
    if will_loop(grid, l, rotate(d), copy.deepcopy(v)):
      found_loops.add(nl)
    grid[nl[0]][nl[1]] = 'X'
  l = nl

c = set()
for i in v:
  c.update(v[i])

print('q1:', len(c))
print('q2:', len(found_loops))