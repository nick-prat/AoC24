import sys

def is_up(r, i, e, u):
  i = max(0, i)
  if i == len(r) - 1:
    return True

  diff = r[i+1] - r[i]

  if diff in ([1,2,3] if u else [-1,-2,-3]):
    return is_up(r, i+1, e, u)
  
  if e == 0:
    return False
  return is_up(r[0:i] + r[i+1:], i-1, e-1, u) or is_up(r[0:i+1] + r[i+2:], i, e-1, u)

reports = [[int(x) for x in line.strip().split(' ')] for line in sys.stdin]

def is_safe(report, err_lim):
  return is_up(report, 0, err_lim, True) or is_up(report, 0, err_lim, False)

err_lim = 1
safe = 0
for report in reports:
  if is_safe(report, err_lim):
    safe += 1
  
print(safe)
