


with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

solution_1= 0
for line in lines:
    game, cubes = line.strip().split(': ')
    _, game_id = game.split(' ')
    skip = False
    for game_set in cubes.split('; '):
        for cube_set in game_set.split(', '):
            count, color = cube_set.split(' ')
            if int(count) > limits[color]:
                skip = True
                continue
        if skip:
            continue
    if skip:
        continue

    solution_1 += int(game_id)

print(solution_1)

solution_2 = 0
for line in lines:
    game, cubes = line.strip().split(': ')
    _, game_id = game.split(' ')
    maxes = {
        'red': 1,
        'green': 1,
        'blue': 1
    }
    for game_set in cubes.split('; '):
        for cube_set in game_set.split(', '):
            count, color = cube_set.split(' ')
            maxes[color] = max(maxes[color], int(count))
    power = maxes['red'] * maxes['green'] * maxes['blue']
    solution_2 += power

print(solution_2)



