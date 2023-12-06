from functools import reduce

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

times = [int(x) for x in lines[0].split(':')[1].strip().split()]
dists = [int(x) for x in lines[1].split(':')[1].strip().split()]


def solve(t, d):
    # binary search between 0 and t // 2
    i = 0
    j = t // 2
    mid = i

    # edge cases
    if d == 0:
        return t
    if j * (t - j) < d:
        return 0

    while i < j:
        mid = (i + j) // 2
        # found
        if (mid-1) * (t - mid + 1) <= d < mid * (t - mid):
            break
        # search right
        elif mid * (t - mid) <= d:
            i = mid + 1
        # search left
        elif mid * (t - mid) > d:
            j = mid

    # return range
    return t - 2 * mid + 1


solution_1 = reduce(lambda x, y: x * y, map(lambda z: solve(times[z], dists[z]), range(len(times))))
print(solution_1)

solution_2 = solve(int(reduce(lambda x, y: str(x) + str(y), times)), int(reduce(lambda x, y: str(x) + str(y), dists)))
print(solution_2)
