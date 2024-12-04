
with (open('input.txt', 'r') as input_file):
    lines = input_file.readlines()

X, Y = len(lines), len(lines[0].strip())
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def solve_1():
    sol = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        j = line.find('X')
        while j > -1:
            found = 0
            for dir in dirs:
                for k in range(1, 4):
                    x, y = i + k * dir[0], j + k * dir[1]
                    if x < 0 or y < 0 or x >= X or y >= Y or lines[x][y] != 'XMAS'[k]:
                        break
                else:
                    found += 1
            sol += found
            j = line.find('X', j+1)
    return sol


def solve_2():
    sol = 0
    for i in range(len(lines)):
        line = lines[i].strip()
        j = line.find('A')
        while j > -1:
            if i-1 >= 0 and j-1 >= 0 and i+1 < X and j+1 < Y:
                a = lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S' or lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M'
                b = lines[i-1][j+1] == 'M' and lines[i+1][j-1] == 'S' or lines[i-1][j+1] == 'S' and lines[i+1][j-1] == 'M'
                if a and b:
                    sol += 1
            j = line.find('A', j+1)
    return sol


print(solve_1())
print(solve_2())
