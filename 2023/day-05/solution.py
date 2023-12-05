import sys

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

seeds = []
indices = {
    'seed-to-soil': 0,
    'soil-to-fertilizer': 1,
    'fertilizer-to-water': 2,
    'water-to-light': 3,
    'light-to-temperature': 4,
    'temperature-to-humidity': 5,
    'humidity-to-location': 6
}
ranges = [list()]*7


i = 0
while i < len(lines):
    if i == 0:
        seeds = [int(x) for x in lines[i].strip().split(': ')[1].split()]
        i += 2
        continue

    split = lines[i].split()
    if len(split) == 2:
        map_name = split[0]
        i += 1
        ranges[indices[map_name]] = list()
        while i < len(lines) and lines[i] != '\n':
            source, dest, length = (int(x) for x in lines[i].strip().split())
            ranges[indices[map_name]].append((source, dest, length))
            i += 1
        ranges[indices[map_name]].sort(key=lambda x: x[1])
    i += 1


def find_location(seed_value, seed_range):
    curr_seed = seed_value
    min_loc = sys.maxsize
    while curr_seed < seed_value + seed_range:
        accounted_here = seed_range
        num = ans = curr_seed
        for index in range(7):
            range_list = ranges[index]
            for range_index, r in enumerate(range_list):
                if r[1] <= num < r[1] + r[2]:
                    ans = r[0] + num - r[1]
                    accounted_here = min(accounted_here, r[1] + r[2] - num)
                    break
                if r[1] > num:
                    ans = num
                    accounted_here = min(accounted_here, r[1] - num)
                    break
                if range_index == len(range_list)-1:
                    accounted_here = min(accounted_here, seed_range)
            num = ans
        min_loc = min(min_loc, ans)
        curr_seed += accounted_here
    return min_loc


solution_1 = sys.maxsize
for seed in seeds:
    solution_1 = min(solution_1, find_location(seed, 1))

print(solution_1)

solution_2 = sys.maxsize
for seed_index in range(0, len(seeds), 2):
    solution_2 = min(solution_2, find_location(seeds[seed_index], seeds[seed_index+1]))

print(solution_2)


