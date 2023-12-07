def solution(data):
    vals = []
    with open(data, 'r') as file:
        for line in file.readlines():
            digits = [char for char in line if char.isdigit()]
            first = digits[0]
            last = digits[-1]
            num = int(first + last)
            vals.append(num)
    return sum(vals)


def solution2(data):
    vals = []
    digits = {'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    reversed_digits = {k[::-1]: v for k, v in digits.items()}
    with open(data, 'r') as file:
        for line in file.readlines():  
            words = [(line.index(digit), str(digits[digit])) for digit in digits if digit in line]
            words += [(len(line) - line[::-1].index(digit) - 1, str(reversed_digits[digit])) for digit in reversed_digits if digit in line[::-1]]
            # if len(words) > 0:
                # new_line = line.replace(words[0][1], str(digits[words[0][1]]))
                # line = new_line.replace(words[-1][1], str(digits[words[-1][1]]))

            nums = [(idx, char) for idx, char in enumerate(line) if char.isdigit()]
            nums.extend(words)
            nums.sort(key=lambda x: x[0])
            # print(nums)
            first = nums[0][1]
            last = nums[-1][1]
            num = int(first + last)
            vals.append(num)
            print(line.strip(), first, last)
            # print(vals)
    return sum(vals)
            
print(solution('./data/sample1.txt'))
print(solution('./data/test1.txt'))

# print(solution2('./data/sample1.txt'))
# print(solution2('./data/test1.txt'))

