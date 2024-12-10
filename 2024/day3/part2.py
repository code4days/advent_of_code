import re

use_example_input = False

if use_example_input:
    input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
else:
    input = open("day3_input.txt").read()


def calculate_result(mem_str):
    matches = re.findall(r"mul\((\d+),(\d+)\)", mem_str)
    return sum([int(match[0]) * int(match[1]) for match in matches])


result = 0
donts = input.split("don't()")

# Since input starts with mul enabled we calcuate that first
result += calculate_result(donts[0])

for part in donts[1:]:
    dos = part.split("do()")
    if len(dos) > 1:
        for do in dos[1:]:
            result += calculate_result(do)

print(result)
