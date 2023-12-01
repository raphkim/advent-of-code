numbers = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}
words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

solution_1 = 0
for line in lines:
    i = 0
    j = len(line) - 1
    while line[i] not in numbers:
        i += 1
    while line[j] not in numbers:
        j -= 1

    number = numbers[line[i]] * 10 + numbers[line[j]]
    solution_1 += number

print(solution_1)

solution_2 = 0
for line in lines:
    first = None
    last = None
    curr = None
    for i in range(len(line)):
        if line[i] in numbers:
            curr = numbers[line[i]]
        elif i + 3 < len(line) and line[i:i+3] in words:
            curr = words[line[i:i+3]]
        elif i + 4 < len(line) and line[i:i+4] in words:
            curr = words[line[i:i+4]]
        elif i + 5 < len(line) and line[i:i+5] in words:
            curr = words[line[i:i+5]]

        if curr is not None:
            if first is None:
                first = curr
            last = curr

        curr = None

    solution_2 += first * 10 + last

print(solution_2)
