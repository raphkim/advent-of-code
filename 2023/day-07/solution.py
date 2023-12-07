from functools import cmp_to_key

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

data = []
for line in lines:
    left, right = line.split()
    data.append([[x for x in left], int(right)])


def card_order(a, b, joker=False):
    if joker:
        order = 'J23456789TQKA'
    else:
        order = '23456789TJQKA'
    return order.find(b) - order.find(a)

def count_cards(hand, joker=False):
    counts = dict()
    jokers = 0
    for card in hand:
        if joker and card == 'J':
            jokers += 1
        elif card not in counts:
            counts[card] = 1
        else:
            counts[card] += 1
    if joker:
        if jokers == 5:
            best = 'A'
            counts[best] = 0
        else:
            best = max(counts, key=counts.get)
        counts[best] += jokers

    return counts


def order_hand(a, b, joker=False):
    a_count = count_cards(a, joker)
    b_count = count_cards(b, joker)
    a_max = max(b_count.values())
    b_max = max(a_count.values())
    # differentiate n of a kind
    if b_max != a_max:
        return a_max - b_max
    # differentiate full house vs three of a kind and two pair vs one pair
    if len(a_count) != len(b_count):
        return len(a_count) - len(b_count)
    # differentiate same types
    for i in range(5):
        if a[i] != b[i]:
            return card_order(a[i], b[i], joker)
    return 0


solution_1 = 0
data.sort(key=cmp_to_key(lambda a, b: order_hand(a[0], b[0])), reverse=True)
for i, item in enumerate(data):
    solution_1 += (i+1) * item[1]
print(solution_1)


solution_2 = 0
data.sort(key=cmp_to_key(lambda a, b: order_hand(a[0], b[0], True)), reverse=True)
for i, item in enumerate(data):
    solution_2 += (i+1) * item[1]
print(solution_2)
