import sys

def is_safe(diffs):
  if diffs[0] == 0:
    return False

  if diffs[0] < 0:
    return all([x < 0 and x >= -3 for x in diffs])
  else:
    return all([x > 0 and x <= 3 for x in diffs]) 
    

reports = [[int(x) for x in line.strip().split(' ')] for line in sys.stdin]

safe = 0
for report in reports:
  diff = []
  for x in range(1, len(report)):
    diff.append(report[x] - report[x-1])
  if is_safe(diff):
    safe += 1
  
print(safe)
