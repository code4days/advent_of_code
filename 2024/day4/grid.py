from collections import defaultdict

grid = defaultdict(str) | {
    (i, j): c for i, r in enumerate(open(0)) for j, c in enumerate(r)
}

directions = -1, 0, 1
search_str = "XMAS"
for i, j in grid.keys():
    for di in directions:
        for dj in directions:
            for n in range(4):
                grid[i + di * n, j + dj * n] in search_str
                print(f"{i} + {di} * {n}, {j} + {dj} * {n}")
