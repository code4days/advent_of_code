use_example_input = False

if use_example_input:
    input = """7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9"""
    input = input.split("\n")
else:
    input = open("day2_input.txt").readlines()


def is_safe(levels):
    diffs = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # all values must be either increasing or decreasing
    all_increasing = all(diff in range(1, 4) for diff in diffs)
    all_decreasing = all(diff in range(-3, 0) for diff in diffs)

    return all_increasing or all_decreasing


safe_count = 0
for line in input:
    levels = [int(num) for num in line.split()]

    if is_safe(levels):
        safe_count += 1
        continue

    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i + 1 :]):
            safe_count += 1
            break


print(f"Safe: {safe_count}")
