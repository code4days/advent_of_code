# grid = open("example_input.txt").readlines()
grid = open("input.txt").read().strip().split("\n")


def find_start(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "^":
                return row, col


row, col = find_start(grid)
row_len, col_len = len(grid), len(grid[row])
# direction are up, right, down, left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
visited = set()

while True:
    visited.add((row, col))
    next_row = row + directions[dir][0]
    next_col = col + directions[dir][1]

    if not (0 <= next_row < row_len and 0 <= next_col < col_len):
        break

    if grid[next_row][next_col] == "#":
        dir = (dir + 1) % len(directions)
        continue

    row, col = next_row, next_col

print(len(visited))
