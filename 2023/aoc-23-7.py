from collections import Counter

def custom_sort(item):
    strength = {'A':13, 'K':12, 'Q':11, 'J':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1}
    key = item[0]
    bid = item[1][0]
    types = item[1][1]
    print([type for type in types] )
    if len(types) > 0:
        max_type = max(type[1] for type in types)
    else:
        max_type = 0
    # print(key, max_type)
    # print(sum(strength[type[0]] for type in types))
    return (max_type, [strength[type[0]] for type in types])

def solution(file):
    hands = {}
    ranks = []

    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            key, val = line.strip().split(' ')
            elem_counts = Counter(key)
            # print(dict(elem_counts))
            types = [(key, val) for key, val in elem_counts.items() if val >= 2]
            print(types)
            hands[key] = (int(val), types)
    # print(hands)

   
    ranks = dict(sorted(hands.items(), key=custom_sort))
    print(ranks)
    rank = 1
    sum = 0
    for key, val in ranks.items():
        sum += rank*val[0]
        rank += 1

    return sum


def solution2(file):
    pass

print(solution('./data/sample7.txt'))
print(solution('./data/test7.txt'))

# print(solution2('./data/sample7.txt'))
# print(solution2('./data/test7.txt'))

