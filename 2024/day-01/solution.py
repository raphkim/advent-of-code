from collections import Counter

lefts, rights = [], []

with (open('input.txt', 'r') as input_file):
    lines = input_file.readlines()

for line in lines:
    l, r = line.split()
    lefts.append(int(l))
    rights.append(int(r))

solution_1 = 0
for left, right in zip(sorted(lefts), sorted(rights)):
    solution_1 += abs(left - right)

print(solution_1)

solution_2 = 0
freq = Counter(rights)

for left in lefts:
    solution_2 += freq[left] * left

print(solution_2)
