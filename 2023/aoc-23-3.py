def check_is_part_num(row, col, schema):
    rows = len(schema)
    cols = len(schema[0])

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if (i, j) != (row, col) and not schema[i][j] == '.' and not schema[i][j].isdigit() and not schema[i][j] == '\n':
                return True
    return False

def solution(data):
    schema = []
    with open(data, 'r') as file:
        schema = [line.strip() for line in file]

    part_nums = []
    for row in range(len(schema)):
        num = ''
        is_part = False
        for col in range(len(schema[row])):
            if schema[row][col].isdigit():
                num += schema[row][col]
                # #print(num)
                is_part = is_part or check_is_part_num(row, col, schema)
                # #print(is_part)
            elif not schema[row][col].isdigit() and schema[row][col] != '.':
                if is_part:
                    part_nums.append(int(num))
                    num = ''
                    is_part = False
                else:
                    continue
            elif schema[row][col] == '.':
                if is_part:
                    part_nums.append(int(num))
                num = ''
                is_part = False
            else:
                num = ''
                is_part = False
        if is_part:
            part_nums.append(int(num))
            num = ''
            is_part = False
    
    print(part_nums)
    return sum(part_nums)



def solution2(data):
    schema = []
    with open(data, 'r') as file:
        schema = [line.strip() for line in file]

    part_nums = []
    for row in range(len(schema)):
        num = ''
        is_part = False
        for col in range(len(schema[row])):
            if schema[row][col].isdigit():
                num += schema[row][col]
                # #print(num)
                is_part = is_part or check_is_part_num(row, col, schema)
                # #print(is_part)
            elif not schema[row][col].isdigit() and schema[row][col] != '.':
                if is_part:
                    part_nums.append(int(num))
                    num = ''
                    is_part = False
                else:
                    continue
            elif schema[row][col] == '.':
                if is_part:
                    part_nums.append(int(num))
                num = ''
                is_part = False
            else:
                num = ''
                is_part = False
        if is_part:
            part_nums.append(int(num))
            num = ''
            is_part = False

print(solution('./data/sample3.txt'))
print(solution('./data/test3.txt'))

# #print(solution2('./data/sample3.txt'))
# #print(solution2('./data/test3.txt'))

