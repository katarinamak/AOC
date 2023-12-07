def solution(file):
    time = []
    top_distances = []
    with open(file, 'r') as input_file:
        input = input_file.read().split('\n')
        time = input[0].split(':')[-1].strip().split()
        top_distances = input[1].split(':')[-1].strip().split()

    ways_to_win = []

    for i, race_t in enumerate(time): # loop through each race
        winners = 0
        for speed in range(int(race_t) + 1): # number of seconds to hold the button down
            t = int(race_t) - speed
            dist = speed * t
            print(top_distances)
            if dist >= int(top_distances[i]):
                winners += 1
        ways_to_win.append(winners)

    print(time)
    print(top_distances)
    prod = 1
    for w in ways_to_win:
        prod *= w

    return prod
    
def solution2(file):
    time = []
    distance = []
    with open(file, 'r') as input_file:
        input = input_file.read().split('\n')
        time = input[0].split(':')[-1].strip().split()
        top_distances = input[1].split(':')[-1].strip().split()

    ways_to_win = []

    for i, race_t in enumerate(time): # loop through each race
        winners = 0
        for speed in range(int(race_t) + 1): # number of seconds to hold the button down
            t = int(race_t) - speed
            dist = speed * t
            # print(top_distances)
            if dist >= int(top_distances[i]):
                winners += 1
        ways_to_win.append(winners)

    prod = 1
    for w in ways_to_win:
        prod *= w

    print(time)
    print(top_distances)

    return prod

# print(solution('./data/sample6.txt'))
# print(solution('./data/test6.txt'))

print(solution2('./data/sample6.txt'))
print(solution2('./data/test6.txt'))

