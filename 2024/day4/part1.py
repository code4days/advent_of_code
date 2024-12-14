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

SEARCH_STR = ["X", "M", "A", "S"]


def check_row_right(grid, row, col):
    for i in range(1, len(SEARCH_STR)):
        next_col = col + i
        if next_col >= len(grid[row]) or grid[row][next_col] != SEARCH_STR[i]:
            return False

    return True


def check_row_left(grid, row, col):
    for i in range(1, len(SEARCH_STR)):
        prev_col = col - i
        if prev_col < 0 or grid[row][prev_col] != SEARCH_STR[i]:
            return False

    return True


def check_col_up(grid, row, col):
    for i in range(1, len(SEARCH_STR)):
        prev_row = row - i
        if prev_row < 0 or grid[prev_row][col] != SEARCH_STR[i]:
            return False

    return True


def check_col_down(grid, row, col):
    for i in range(1, len(SEARCH_STR)):
        next_row = row + i
        if next_row == len(grid) or grid[next_row][col] != SEARCH_STR[i]:
            return False

    return True


def check_right_diagonal_up(grid, row, col):
    for i in range(1, len(SEARCH_STR)):
        next_row = row - i
        next_col = col + i
        if (
            next_row < 0
            or next_col == len(grid[row])
            or grid[next_row][next_col] != SEARCH_STR[i]
        ):
            return False

    return True


def check_right_diagonal_down(grid, row, col):
    for i in range(1, len(SEARCH_STR)):
        next_row = row + i
        next_col = col + i
        if (
            next_row == len(grid)
            or next_col == len(grid[row])
            or grid[next_row][next_col] != SEARCH_STR[i]
        ):
            return False

    return True


def check_left_diagonal_up(grid, row, col):
    for i in range(1, len(SEARCH_STR)):
        next_row = row - i
        next_col = col - i
        if next_row < 0 or next_col < 0 or grid[next_row][next_col] != SEARCH_STR[i]:
            return False
    return True


def check_left_diagonal_down(grid, row, col):
    for i in range(1, len(SEARCH_STR)):
        next_row = row + i
        next_col = col - i
        if (
            next_row == len(grid)
            or next_col < 0
            or grid[next_row][next_col] != SEARCH_STR[i]
        ):
            return False

    return True


grid = [line.strip() for line in input.split("\n")[:-1]]
total = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == SEARCH_STR[0]:
            total += sum(
                [
                    check_row_right(grid, row, col),
                    check_row_left(grid, row, col),
                    check_col_up(grid, row, col),
                    check_col_down(grid, row, col),
                    check_right_diagonal_up(grid, row, col),
                    check_right_diagonal_down(grid, row, col),
                    check_left_diagonal_up(grid, row, col),
                    check_left_diagonal_down(grid, row, col),
                ]
            )
print(f"Total: {total}")
