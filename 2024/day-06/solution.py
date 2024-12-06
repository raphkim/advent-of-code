
with (open('input.txt', 'r') as input_file):
    lines = input_file.readlines()

ds = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid = [['+'] + [c for c in row.strip()] + ['+'] for row in lines]
grid += [['+' for _ in grid[0]]]
grid = [['+' for _ in grid[0]]] + grid

start = None
for r, row in enumerate(grid):
    for c, col in enumerate(row):
        if col == '^':
            grid[r][c] = '.'
            start = (r, c)
            break
    if start:
        break


def walk(m):
    new = [row[:] for row in m]
    i, j = start
    d = 0
    while new[i][j] != '+':
        turned = False
        if new[i][j] == '.':
            new[i][j] = str(d)
        while new[i+ds[d][0]][j+ds[d][1]] == '#':
            turned = True
            d = (d + 1) % 4
        if str(d) in new[i][j] and turned:
            # loop detected!
            return new, True
        if str(d) not in new[i][j]:
            new[i][j] += str(d)
        i += ds[d][0]
        j += ds[d][1]
    return new, False


sol1, sol2 = 0, 0
g, _ = walk(grid)

# part 1
for row in g:
    for col in row:
        if col.isnumeric():
            sol1 += 1
print(sol1)

# part 2
for r, row in enumerate(g):
    for c, col in enumerate(row):
        if col.isnumeric():
            grid[r][c] = '#'
            _, loop = walk(grid)
            grid[r][c] = '.'
            if loop:
                sol2 += 1
print(sol2)
