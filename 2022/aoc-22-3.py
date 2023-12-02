
def solution(data):
    rucksacks = {}
    r_num = 1
    with open(data) as input:
        for line in input.readlines():
            idx = len(line)//2
            rucksacks[r_num] = (line[:idx], line[idx:])
            r_num += 1

    # print(rucksacks)
    common = []
    for c1, c2 in rucksacks.values():
        common.append(set(c1) & set(c2))
    
    sum = 0

    for chars_set in common:
        for c in chars_set:
            if c.isupper():
                sum += ord(c) - ord('A') + 27
            elif c.islower():
                sum += ord(c) - ord('a') + 1

    return sum


def solution2(data):
    rucksacks = {}
    r_num = 1
    with open(data) as input:
        for line in input.readlines():
            if r_num in rucksacks:
                rucksacks[r_num].append(line.strip('\n'))
            else:
                rucksacks[r_num] = [line.strip('\n')]

            if len(rucksacks[r_num]) == 3:
                r_num += 1
            


    common = []
    for rucksack in rucksacks.values():
        common_chars = set(rucksack[0])
        for r in rucksack[1:]:
            common_chars &= set(r)
        common.append(common_chars)
    
    sum = 0

    for chars_set in common:
        for c in chars_set:
            if c.isupper():
                sum += ord(c) - ord('A') + 27
            elif c.islower():
                sum += ord(c) - ord('a') + 1

    return sum

# print(solution('./data/sample3.txt'))
# print(solution('./data/test3.txt'))

print(solution2('./data/sample3.txt'))
print(solution2('./data/test3.txt'))

