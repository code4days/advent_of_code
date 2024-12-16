"""
Refactor after looking at better answers on reddit
Prints answers for both parts
"""

from functools import cmp_to_key

# idea is we sort each pages line and compare to original if its the same
# the pages are in the right order otherwise they aren't

# rules, pages = open("example_input.txt").read().split("\n\n")
rules, pages = open("input.txt").read().split("\n\n")

rules = {tuple(rule.split("|")) for rule in rules.split()}
# same thing: {(*rule.split("|"),) for rule in rules.split()}


cmp = cmp_to_key(lambda x, y: -1 if ((x, y) in rules) else 1)
# 4HbQ used math to return -1 or 1
# cmp = cmp_to_key(lambda x, y: 1 - 2 * ((x, y) in rules))


answers = [0, 0]
# for page in pages.split():
#     page = page.split(",")
#     sorted_pages = sorted(page, key=cmp)
#     if page == sorted_pages:
#         answers[0] += int(sorted_pages[len(sorted_pages) // 2])
#     else:
#         answers[1] += int(sorted_pages[len(sorted_pages) // 2])

for page in pages.split():
    page = page.split(",")
    sorted_pages = sorted(page, key=cmp)
    # user 4HbQ brilliantly used bools as keys
    answers[page != sorted_pages] += int(sorted_pages[len(sorted_pages) // 2])

print(*answers)
