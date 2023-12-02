import sys
import os

def generate_template(num):
    filename = f'aoc-23-{num}.py'
    template = ''
    template += f'def solution(data):\n'
    template += '    pass\n\n'

    template += f'def solution2(data):\n'
    template += '    pass\n\n'

    template += f'# print(solution(\'./2023/data/sample{num}.txt\'))\n'
    template += f'# print(solution(\'./2023/data/test{num}.txt\'))\n\n'

    template += f'print(solution2(\'./2023/data/sample{num}.txt\'))\n'
    template += f'print(solution2(\'./2023/data/test{num}.txt\'))\n\n'


    with open(filename, 'w') as file:
        file.write(template)

    with open(f'./2023/data/sample{num}.txt', 'w') as sample_data:
        pass

    with open(f'./2023/data/test{num}.txt', 'w') as sample_data:
        pass

    

if __name__ == "__main__":
    generate_template(sys.argv[1])