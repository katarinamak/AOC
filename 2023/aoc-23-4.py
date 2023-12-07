def find_intersection(s1, s2):
    nums1 = s1.strip().split(' ')
    nums2 = s2.strip().split(' ')
    intersection = list(set(nums1) & set(nums2))
    intersection = [int(num) for num in intersection if num != '']
    return intersection


def solution(file):
    cards = []
    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            new_line = line.split(':')[-1].strip()
            s1, s2 = new_line.split('|')
            cards.append(find_intersection(s1, s2))
    points = 0
    for c in cards:
        if len(c) > 0:
            points += 2**(len(c) - 1)
    return points


def solution2(file):
    cards = []
    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            new_line = line.split(':')[-1].strip()
            s1, s2 = new_line.split('|')
            cards.append(find_intersection(s1, s2))
    
    copies = {}
    copies = {index + 1: 1 for index, _ in enumerate(cards)}
    for i, c in enumerate(cards):
        matches = len(c)
        for j in range(1, matches + 1):
            key = i + 1 + j
            copies[key] += copies[i + 1]

    return sum(copies.values())

# print(solution('./data/sample4.txt'))
# print(solution('./data/test4.txt'))

print(solution2('./data/sample4.txt'))
print(solution2('./data/test4.txt'))

