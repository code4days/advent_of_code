from collections import defaultdict

use_example_input = False

if use_example_input:
    input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
else:
    input = open("day5_input.txt").read()


rules = defaultdict(set)
pages_to_produce = []
total = 0

parse_rules = True
for line in input.split("\n"):
    if not line:
        parse_rules = False
        continue

    if parse_rules:
        k, v = line.split("|")
        rules[k].add(v)
    else:
        pages = line.split(",")
        for i, page in enumerate(pages):
            if not set(pages[i + 1 :]) <= rules[page]:
                sorted_pages = sorted(
                    pages,
                    key=lambda item: (
                        sum(1 for other in pages if item in rules[other]),
                    ),
                )
                total += int(sorted_pages[len(sorted_pages) // 2])
                break


print(total)
