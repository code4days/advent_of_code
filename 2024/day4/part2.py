use_example_input = False

if use_example_input:
    input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""
else:
    input = open("day4_input.txt").read()


def check_right_diagonal(grid, row, col):
    if row == 0 or row == len(grid[row]) - 1:
        return False
    if col == 0 or col == len(grid[row]) - 1:
        return False

    word = grid[row - 1][col + 1] + grid[row][col] + grid[row + 1][col - 1]

    return word == "MAS" or word[::-1] == "MAS"


def check_left_diagonal(grid, row, col):
    if row == 0 or row == len(grid[row]) - 1:
        return False
    if col == 0 or col == len(grid[row]) - 1:
        return False

    word = grid[row - 1][col - 1] + grid[row][col] + grid[row + 1][col + 1]
    return word == "MAS" or word[::-1] == "MAS"


def has_mas(grid, row, col):
    if check_left_diagonal(grid, row, col) and check_right_diagonal(grid, row, col):
        return True

    return False


grid = [line.strip() for line in input.split("\n")[:-1]]
total = 0

for row in range(1, len(grid) - 1):
    for col in range(len(grid[row])):
        if grid[row][col] == "A":
            if has_mas(grid, row, col):
                total += 1


print(f"Total: {total}")
