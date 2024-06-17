example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def find_symbols(row, col, num, grid):
    num_len = len(num)
    delta_row = [0, *[1] * (num_len + 2), 0, *[-1] * (num_len + 2)]
    delta_col = [
        0,
        *range(0, -(num_len + 1), -1),
        *[-(num_len + 1)] * 3,
        *range(-(num_len), 1, 1),
    ]

    for i in range(len(delta_row)):
        next_row = row + delta_row[i]
        next_col = col + delta_col[i]
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[row]):
            char = grid[next_row][next_col]
            if char != "." and not char.isdigit():
                return True
    return False


grid = open("day3_input.txt").readlines()
# grid = example.split("\n")
total = 0
for row in range(0, len(grid)):
    num = []
    for col in range(0, len(grid[row].strip())):
        char = grid[row][col]
        if char.isdigit():
            num.append(char)
        elif num:
            if find_symbols(row, col, num, grid):
                total += int("".join(num))

            # determine if its a part number
            num = []
        if col == len(grid[row].strip()) - 1 and find_symbols(row, col, num, grid):
            total += int("".join(num))
print(total)
