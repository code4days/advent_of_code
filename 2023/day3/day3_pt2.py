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

visited = set()


def find_digits(digit_coords, grid):
    """
    Find digits surrounding that make up the number
    the passed in digit is part of, we add visited coords
    to a set to avoid revisiting them again
    """
    row, col = digit_coords
    digits = []
    left_index, right_index = 0, len(grid[row]) - 1
    # look_left
    for i in range(col, -1, -1):
        if not grid[row][i].isdigit():
            left_index = i + 1
            break
        visited.add((row, i))
    # look_right
    for i in range(col, len(grid[row])):
        if not grid[row][i].isdigit():
            right_index = i
            break
        visited.add((row, i))
    digits.append(grid[row][left_index:right_index])
    return digits


def find_numbers(row, col, grid):
    """
    Find the numbers adjacent to a * char
    """
    delta_row = [-1, -1, -1, 0, 1, 1, 1, 0]
    delta_col = [-1, 0, 1, 1, 1, 0, -1, -1]
    numbers = []

    for i in range(len(delta_row)):
        next_row = row + delta_row[i]
        next_col = col + delta_col[i]
        if (next_row, next_col) in visited:
            continue
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[row]):
            char = grid[next_row][next_col]
            if char.isdigit():
                digits = find_digits((next_row, next_col), grid)
                numbers.append(int("".join(digits)))
    return numbers


print("start")
grid = open("day3_input.txt").readlines()
# grid = example.split("\n")
total = 0
for row in range(0, len(grid)):
    for col in range(0, len(grid[row].strip())):
        char = grid[row][col]
        if char == "*":
            numbers = find_numbers(row, col, grid)
            print(f"numbers: {numbers}")
            if len(numbers) > 1:
                total += numbers[0] * numbers[1]

print("end")
print(f"total: {total}")
