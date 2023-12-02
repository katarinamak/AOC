from enum import Enum


def solution(data):
    p1 = []
    p2 = []

    with open(data) as input:
        for line in input.readlines():
            moves = line.split(' ')
            p1.append(moves[0].strip('\n'))
            p2.append(moves[1].strip('\n'))
    

    shapes = {'X': 1, 'Y': 2, 'Z': 3}
        
    
    moves = {('A', 'X'): 3, ('A', 'Y'): 6, ('A', 'Z'): 0, 
            ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
            ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3}

    total_score = 0

    for i in range(len(p1)):
        outcome = moves[(p1[i], p2[i])]
        total_score += (shapes[p2[i]] + outcome)

    return total_score

def solution2(data):
    p1 = []
    p2 = []

    with open(data) as input:
        for line in input.readlines():
            moves = line.split(' ')
            p1.append(moves[0].strip('\n'))
            p2.append(moves[1].strip('\n'))
        
    
    moves = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8, 
            ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
            ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7}

    total_score = 0

    for i in range(len(p1)):
        total_score += moves[(p1[i], p2[i])]

    return total_score

# print(solution('./data/sample2.txt'))
# print(solution('./data/test2.txt'))

print(solution2('./data/sample2.txt'))
print(solution2('./data/test2.txt'))

