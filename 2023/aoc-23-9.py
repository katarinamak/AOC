def extrapolate(stack):
    if len(stack) >= 2:
        curr = stack.pop()
        prev = stack.pop()
        prev.append(curr[-1] + prev[-1])
        stack.append(prev)
        return extrapolate(stack)
    else:
        return stack[-1][-1]
        

def sequencing(stack):
    seq = stack[-1]
    differences = []
    for i in range(1, len(seq)):
       differences.append(seq[i]- seq[i-1])

    if all(diff == 0 for diff in differences):
        stack.append(differences)
        return extrapolate(stack)
    else:
        stack.append(differences)
        return sequencing(stack)

def solution(file):
    sum = 0
    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            seq = [int(x) for x in line.strip().split()]
            stack = [seq]
            sum += sequencing(stack)

    return sum
            

def extrapolate_backwards(stack):
    if len(stack) >= 2:
        curr = stack.pop()
        prev = stack.pop()
        prev.insert(0, prev[0] - curr[0])
        # print(prev[-1])
        stack.append(prev)
        return extrapolate_backwards(stack)
    else:
        return stack[-1][0]

def sequencing_backwards(stack):
    seq = stack[-1]
    differences = []
    for i in range(1, len(seq)):
       differences.append(seq[i]- seq[i-1])

    if all(diff == 0 for diff in differences):
        stack.append(differences)
        return extrapolate_backwards(stack)
    else:
        stack.append(differences)
        return sequencing_backwards(stack)

def solution2(file):
    sum = 0
    with open(file, 'r') as input_file:
        for line in input_file.readlines():
            seq = [int(x) for x in line.strip().split()]
            stack = [seq]
            sum += sequencing_backwards(stack)

    return sum

# print(solution('./data/sample9.txt'))
# print(solution('./data/test9.txt'))

print(solution2('./data/sample9.txt'))
print(solution2('./data/test9.txt'))

