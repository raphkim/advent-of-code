from functools import reduce
from math import sqrt, ceil

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

times = [int(x) for x in lines[0].split(':')[1].strip().split()]
dists = [int(x) for x in lines[1].split(':')[1].strip().split()]

print("solution 1:", reduce(lambda x, y: x * y, map(lambda z: 2 * ceil(sqrt(times[z]**2-4*dists[z]) / 2) - 1, range(len(times)))))
print("solution 2:", 2 * ceil(sqrt(int(reduce(lambda x, y: str(x)+str(y), times))**2-4*int(reduce(lambda x, y: str(x)+str(y), dists))) / 2) - 1)


# def solve(t, d):
#     # binary search between 0 and t // 2
#     i = 0
#     j = t // 2
#     mid = i
#
#     # edge cases
#     if d == 0:
#         return t
#     if j * (t - j) < d:
#         return 0
#
#     while i < j:
#         mid = (i + j) // 2
#         # found
#         if (mid-1) * (t - mid + 1) <= d < mid * (t - mid):
#             break
#         # search right
#         elif mid * (t - mid) <= d:
#             i = mid + 1
#         # search left
#         elif mid * (t - mid) > d:
#             j = mid
#
#     # return range
#     return t - 2 * mid + 1
#
#
# solution_1 = 1
# for k in range(len(times)):
#     solution_1 *= solve(times[k], dists[k])
# print(solution_1)
#
#
# time = dist = ''
# for k in range(len(times)):
#     time += str(times[k])
#     dist += str(dists[k])
# solution_2 = solve(int(time), int(dist))
# print(solution_2)
