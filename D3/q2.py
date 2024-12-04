import re
import sys

exp = re.compile(r"(?:mul\((\d{1,3}),(\d{1,3})\))|(?:((?:do)|(?:don't))\(\))")

lines = [exp.findall(line) for line in sys.stdin]

sum = 0
accept = True
for line in lines:
    for match in line:
        if match[2] == "do":
            accept = True
        elif match[2] == "don't":
            accept = False
        elif accept:
            sum += int(match[0]) * int(match[1])
print(sum)