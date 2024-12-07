use_example_input = False

if use_example_input:
    input = """7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9"""
else:
    input = open("day2.txt").read()

# input = "1 2 7 8 9"

safe = 0
for line in input.split("\n")[:-1]:
    levels = [int(level) for level in line.split()]

    is_increasing = True
    is_decreasing = True
    for i in range(len(levels) - 1):
        if levels[i + 1] - levels[i] not in range(1, 4):
            is_increasing = False
            break

    if not is_increasing:
        # check for decreasing values
        for i in range(len(levels) - 1):
            if levels[i + 1] - levels[i] not in range(-3, 0):
                is_decreasing = False
                break

    if is_increasing or is_decreasing:
        safe += 1


print(f"Safe: {safe}")
