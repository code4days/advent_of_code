from collections import defaultdict

possible_cubes = {"red": 12, "green": 13, "blue": 14}

all_games = open("day2_input.txt").readlines()
examples = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]
# all_games = examples
total = 0
for game in all_games:
    possible_game = True
    game_id, cubes = game.split(":")
    for draw in cubes.split(";"):
        for color_str in draw.split(","):
            count, color = color_str.split()
            if possible_cubes[color] < int(count):
                possible_game = False
                break
        if not possible_game:
            break
    if possible_game:
        total += int(game_id.split()[1])


print(total)

# part 2


total = 0
for game in all_games:
    game_id, cubes = game.split(":")
    cube_counts = defaultdict(int)
    for draw in cubes.split(";"):
        for color_str in draw.split(","):
            count, color = color_str.split()
            if cube_counts[color] < int(count):
                cube_counts[color] = int(count)

    power = 1
    for _, value in cube_counts.items():
        power *= value
    total += power

print(total)
