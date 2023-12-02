def solution(data):
    count = 0
    for line in open(data).read().splitlines():
        left, right = line.split(',')
        min1, max1 = left.split('-') 
        min2, max2 = right.split('-') 
        if int(min1) <= int(min2) <= int(max2) <= int(max1):
            count += 1
        elif int(min2) <= int(min1) <= int(max1) <= int(max2):
            count += 1
    
    return count

def solution2(data):
    count = 0
    for line in open(data).read().splitlines():
        left, right = line.split(',')
        min1, max1 = left.split('-') 
        min2, max2 = right.split('-') 
        # if int(min1) <= int(min2) <= int(max2) <= int(max1):
        #     count += 1
        # elif int(min2) <= int(min1) <= int(max1) <= int(max2):
        #     count += 1
        if int(min1) <= int(min2) <= int(max1) or int(min1) <= int(max2) <= int(max1) or (int(min2) <= int(min1) <= int(max2)):
            # print('YES', line)
            count += 1
        else:
            print('NO', line)

    return count

# print(solution('./data/sample4.txt'))
# print(solution('./data/test4.txt'))

print(solution2('./data/sample4.txt'))
print(solution2('./data/test4.txt'))

