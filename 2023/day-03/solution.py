with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
adjacent_dirs = {
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
}

solution_1 = 0
for i, line in enumerate(lines):
    for j in range(len(line)):
        if line[j] not in numbers or j > 0 and line[j-1] in numbers:
            continue
        has_symbol = False
        number = ''
        curr = j
        while line[curr] in numbers:
            number += line[curr]
            for adjacent_dir in adjacent_dirs:
                try:
                    adjacent_char = lines[i+adjacent_dir[0]][curr+adjacent_dir[1]]
                    if adjacent_char not in numbers and adjacent_char != '.' and adjacent_char != '\n':
                        has_symbol = True
                except IndexError:
                    pass
            curr += 1
            if curr >= len(line):
                break

        if has_symbol:
            solution_1 += int(number)

print(solution_1)


def find_left_and_right(_lines, _i, _j):
    _curr = _j - 1
    _left = ''
    while _curr >= 0 and _lines[_i][_curr] in numbers:
        _left = _lines[_i][_curr] + _left
        _curr -= 1

    _curr = _j + 1
    _right = ''
    while _curr < len(_lines[_i]) and _lines[_i][_curr] in numbers:
        _right += _lines[_i][_curr]
        _curr += 1

    return _left, _right


solution_2 = 0
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != '*':
            continue
        ratios = []

        left, right = find_left_and_right(lines, i, j)

        if len(left) > 0:
            ratios.append(int(left))
        if len(right) > 0:
            ratios.append(int(right))

        if i > 0:
            left, right = find_left_and_right(lines, i-1, j)

            above = ''
            if lines[i-1][j] in numbers:
                above = left + lines[i-1][j] + right
            if len(above) > 0:
                ratios.append(int(above))
            else:
                if len(left) > 0:
                    ratios.append(int(left))
                if len(right) > 0:
                    ratios.append(int(right))

        if i < len(lines) - 1:
            left, right = find_left_and_right(lines, i+1, j)

            below = ''
            if lines[i+1][j] in numbers:
                below = left + lines[i+1][j] + right
            if len(below) > 0:
                ratios.append(int(below))
            else:
                if len(left) > 0:
                    ratios.append(int(left))
                if len(right) > 0:
                    ratios.append(int(right))

        if len(ratios) == 2:
            solution_2 += ratios[0] * ratios[1]

print(solution_2)


