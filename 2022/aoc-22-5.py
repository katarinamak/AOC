import parse


def solution(data):
    crates = {}

    stacks, instructions = open(data).read().split('\n\n')

    
    for line in stacks.splitlines()[:-1]:
        for i, c in enumerate(line[1::4]):
            if c == ' ':
                continue
            if i+1 not in crates:
                crates[i+1] = []
            crates[i+1] = [c] + crates[i+1]
    # print(crates)

    for line in instructions.splitlines():
        num_to_move, from_idx, to_idx = parse.parse('move {:d} from {:d} to {:d}', line)

        for i in range(num_to_move):
            top = crates[from_idx].pop()
            # print(top)
            crates[to_idx].append(top)
        # print(crates)

    tops = ''
    for k in sorted(crates):
        tops += crates[k].pop()
    
    return tops

def solution2(data):
    crates = {}

    stacks, instructions = open(data).read().split('\n\n')

    for line in stacks.splitlines()[:-1]:
        for i, c in enumerate(line[1::4]):
            if c == ' ':
                continue
            if i+1 not in crates:
                crates[i+1] = []
            crates[i+1] = [c] + crates[i+1]
    # print(crates)

    for line in instructions.splitlines():
        num_to_move, from_idx, to_idx = parse.parse('move {:d} from {:d} to {:d}', line)

        crates[to_idx].extend(crates[from_idx][-num_to_move:])
        crates[from_idx] = crates[from_idx][:-num_to_move]
        # for i in range(num_to_move):
        #     top = crates[from_idx].pop()
        #     # print(top)
        #     crates[to_idx].append(top)
        # print(crates)

    tops = ''
    for k in sorted(crates):
        tops += crates[k].pop()
    
    return tops

# print(solution('./data/sample5.txt'))
# print(solution('./data/test5.txt'))

print(solution2('./data/sample5.txt'))
print(solution2('./data/test5.txt'))

