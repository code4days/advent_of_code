from collections import defaultdict

# input = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
# """

input = open("input_day1_part1.txt", "r").read()

left_list = []
right_list_counts = defaultdict(int)

# O(n)
for line in input.split("\n")[:-1]:
    n1, n2 = line.split()
    left_list.append(int(n1))
    right_list_counts[int(n2)] += 1


# O(n)
total = 0
for item in left_list:
    if item in right_list_counts:
        total += item * right_list_counts[item]
print(total)
