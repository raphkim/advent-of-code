
with (open('input.txt', 'r') as input_file):
    lines = input_file.readlines()

solution_1 = 0
solution_2 = 0


def is_safe(nums):
    if nums[0] == nums[1]:
        return False
    elif nums[1] - nums[0] < 0:
        nums.reverse()
    prev = nums[0]
    safe = True
    for num in nums[1:]:
        if 0 < num - prev < 4:
            prev = num
        else:
            safe = False
            break
    return safe


for line in lines:
    numbers = [int(x) for x in line.split()]
    if is_safe(numbers):
        solution_1 += 1

print(solution_1)

for line in lines:
    numbers = [int(x) for x in line.split()]
    for i in range(len(numbers)):
        if is_safe(numbers[:i] + numbers[i+1:]):
            solution_2 += 1
            break

print(solution_2)
