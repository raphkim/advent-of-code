from collections import defaultdict

with (open('input.txt', 'r') as input_file):
    lines = input_file.readlines()


pages = []

# contradictions?
afters = defaultdict(list)

switch = False
for line in lines:
    if line == '\n':
        switch = True
        continue

    if switch:
        pages.append(line.strip().split(','))
    else:
        x, y = line.strip().split('|')
        afters[x].append(y)

def reorder(page_list):
    i = 1
    while i < len(page_list):
        if page_list[i-1] in afters[page_list[i]]:
            page_list[i], page_list[i-1] = page_list[i-1], page_list[i]
            if i > 1:
                i -= 1
        else:
            i += 1


def solve():
    sol1, sol2 = 0, 0
    for p in pages:
        good = True
        prev = p[0]
        for page in p[1:]:
            if prev in afters[page]:
                # print('contradiction!', prev, page)
                good = False
            prev = page
        if good:
            sol1 += int(p[len(p)//2])
        else:
            reorder(p)
            sol2 += int(p[len(p)//2])

    return sol1, sol2




print(solve())
