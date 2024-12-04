import re
import sys

exp = re.compile(r"mul\((\d+),(\d+)\)")

lines = [exp.findall(line) for line in sys.stdin]

sum = 0
for line in lines:
    for match in line:
        sum += int(match[0]) * int(match[1])
print(sum)