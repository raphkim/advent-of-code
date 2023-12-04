with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

solution_1 = 0
for line in lines:
    left, right = line.strip().split(': ')[1].split(' | ')
    winning = {int(x) for x in left.split()}
    my_nums = [int(x) for x in right.split()]
    count = 0
    for num in my_nums:
        if num in winning:
            count += 1
    if count > 0:
        solution_1 += (1 << count-1)

print(solution_1)

counts = [1] * len(lines)
for i, line in enumerate(lines):
    left, right = line.strip().split(': ')[1].split(' | ')
    winning = {int(x) for x in left.split()}
    my_nums = [int(x) for x in right.split()]
    wins = 1
    for num in my_nums:
        if num in winning:
            counts[i + wins] += counts[i]
            wins += 1
solution_2 = sum(counts)

print(solution_2)


