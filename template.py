import sys
import os

def generate_template(num):
    filename = f'aoc-22-{num}.py'
    template = ''
    template += f'def solution(data):\n'
    template += '    pass\n\n'

    template += f'def solution2(data):\n'
    template += '    pass\n\n'

    template += f'# print(solution(\'./data/sample{num}.txt\'))\n'
    template += f'# print(solution(\'./data/test{num}.txt\'))\n\n'

    template += f'print(solution2(\'./data/sample{num}.txt\'))\n'
    template += f'print(solution2(\'./data/test{num}.txt\'))\n\n'


    with open(filename, 'w') as file:
        file.write(template)

    with open(f'./data/sample{num}.txt', 'w') as sample_data:
        pass

    with open(f'./data/test{num}.txt', 'w') as sample_data:
        pass

    

if __name__ == "__main__":
    generate_template(sys.argv[1])