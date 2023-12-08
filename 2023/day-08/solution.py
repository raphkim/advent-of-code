import math

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

dirs = []
nodes = {}
for i in range(len(lines)):
    if i == 0:
        dirs = [0 if x == 'L' else 1 for x in lines[i].strip()]
    elif i == 1:
        continue
    else:
        left, right = lines[i].strip().split(' = ')
        nodes[left] = right.removeprefix('(').removesuffix(')').split(', ')


solution_1 = 0
dir_i = 0
curr = 'AAA'
while curr != 'ZZZ':
    curr = nodes[curr][dirs[dir_i]]
    dir_i = (dir_i + 1) % len(dirs)
    solution_1 += 1
print(solution_1)


steps = 0
curr = [x for x in nodes.keys() if x[2] == 'A']
cycles = dict()
done = False
while any(node[2] != 'Z' for node in curr) and not done:
    for i, node in enumerate(curr):
        if node[2] == 'Z' and node not in cycles:
            cycles[node] = steps
            if len(cycles) == len(node):
                done = True
        curr[i] = nodes[curr[i]][dirs[dir_i]]
    dir_i = (dir_i + 1) % len(dirs)
    steps += 1
vals = list(cycles.values())
solution_2 = math.lcm(*vals)
print(solution_2)

