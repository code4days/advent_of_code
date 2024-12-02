use_test_input = False

if use_test_input:
    input = """3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    """
else:
    input = open("input_day1_part1.txt", "r").read()

list1 = []
list2 = []

# O(n)
for line in input.split("\n")[:-1]:
    n1, n2 = line.split()
    list1.append(int(n1))
    list2.append(int(n2))

# O(nlogn)
sorted_list1 = sorted(list1)
sorted_list2 = sorted(list2)

# O(n)
total = 0
for left, right in zip(sorted_list1, sorted_list2):
    total += abs(right - left)

print(f"Total: {total}")
