import sys
import heapq

def solution(data):
    elf_cals = {}
    elf_num = 1
    with open(data) as inputfile:
        for line in inputfile.readlines():
            if line == '\n':
                elf_num += 1
                continue
            
            if elf_num in elf_cals:
                elf_cals[elf_num] += int(line.strip('\n'))
            else:
                elf_cals[elf_num] = int(line.strip('\n'))

    heap = [(-value, key) for key, value in elf_cals.items()]
    heapq.heapify(heap)

    ret = heapq.heappop(heap)
    return (-ret[0], ret[1])

def solution2(data):
    elf_cals = {}
    elf_num = 1
    with open(data) as inputfile:
        for line in inputfile.readlines():
            if line == '\n':
                elf_num += 1
                continue
            
            if elf_num in elf_cals:
                elf_cals[elf_num] += int(line.strip('\n'))
            else:
                elf_cals[elf_num] = int(line.strip('\n'))

    heap = [(-value, key) for key, value in elf_cals.items()]
    heapq.heapify(heap)

    ret = 0
    for i in range(3):
        top = heapq.heappop(heap)
        ret += (-top[0])

    return ret




# print(solution('./data/sample1.txt'))
# print(solution('./data/test1.txt'))

print(solution2('./data/sample1.txt'))
print(solution2('./data/test1.txt'))