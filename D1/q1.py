import sys

i = [[int(x) for x in line.strip().split("   ")] for line in sys.stdin]
a = sorted(list(map(lambda x: x[0], i)))
b = sorted(list(map(lambda x: x[1], i)))

sum = 0
for x in range(0, len(a)):
    sum += abs(a[x] - b[x])

print(sum)