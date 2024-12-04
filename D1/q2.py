import sys

i = [[int(x) for x in line.strip().split("   ")] for line in sys.stdin]
a = map(lambda x: x[0], i)
b = map(lambda x: x[1], i)
bm = {}

for x in b:
    if x in bm:
        bm[x] += 1
    else:
        bm[x] = 1

sum = 0
for x in a:
    sum += x * bm.get(x, 0)

print(sum)