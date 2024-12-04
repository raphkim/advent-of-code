
with (open('input.txt', 'r') as input_file):
    lines = input_file.readlines()


def solve_1(line):
    sol = 0
    i = 0
    while True:
        i = line.find('mul(', i)+4
        j = line.find(')', i)
        if i == 3 or j < 0:
            break
        try:
            a, b = line[i:j].split(',')
            sol += int(a) * int(b)
        except:
            pass

    return sol


def solve_2(line):
    sol = 0
    i = 0
    while True:
        dont = line.find("don't()", i) + 7
        while True:
            i = line.find('mul(', i)+4
            j = line.find(')', i)
            if i == 3 or j < 0 or dont != 6 and i > dont:
                break
            try:
                a, b = line[i:j].split(',')
                sol += int(a) * int(b)
            except:
                pass
        if i == 3:
            break
        i = line.find("do()", dont)
    return sol


print(solve_1(''.join(lines)))
print(solve_2(''.join(lines)))
