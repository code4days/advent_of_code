import re

use_example_input = False

if use_example_input:
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
else:
    input = open("day3_input.txt").read()

matches = re.findall(r"mul\((\d+),(\d+)\)", input)
print(sum([int(match[0]) * int(match[1]) for match in matches]))
