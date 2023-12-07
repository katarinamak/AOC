def solution(data):
    colours = {'red': 12, 'blue': 14, 'green': 13}
    game = 1
    sum = 0
    with open(data, 'r') as file:
        for line in file.readlines():
            idx = line.index(':')
            sets = line.strip()[idx + 1:].split(';')
            print(sets)

            for s in sets:
                cubes = s.strip().split(',')
                possible = True
                for cube in cubes:
                    tokens = cube.strip().split(' ')
                    print(tokens)
                    if int(tokens[0].strip()) > colours[tokens[1].strip()]:
                        possible = False
                        break
                if not possible:
                    break
            if possible:
                sum += game
            game += 1
    return sum

def solution2(data):
    colours = {'red': 0, 'blue': 0, 'green': 0}
    game = 1
    powers = {}
    with open(data, 'r') as file:
        for line in file.readlines():
            idx = line.index(':')
            sets = line.strip()[idx + 1:].split(';')
            # print(sets)

            for s in sets:
                cubes = s.strip().split(',')
                for cube in cubes:
                    tokens = cube.strip().split(' ')
                    # print(tokens)
                    colours[tokens[1].strip()] = max(int(tokens[0].strip()), colours[tokens[1].strip()])
            power = 1
            print(colours)
            for val in colours.values():
                # print(val)
                power *= val
                # print(power)
            powers[game] = power
            game += 1
            colours = {'red': 0, 'blue': 0, 'green': 0}
    return sum(powers.values())

print(solution('./data/sample2.txt'))
print(solution('./data/test2.txt'))

# print(solution2('./data/sample2.txt'))
# print(solution2('./data/test2.txt'))

