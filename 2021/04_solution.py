# https://adventofcode.com/2021/day/4

from pprint import pprint

def _parse_input(input_filename: str) -> list:
    with open(input_filename, "r") as fp:
        result = fp.read()
    return [int(number) for number in result.split('\n\n')[0].split(',')], \
           [[[int(number) for number in line.split()] for line in board.split('\n')] for board in result.split('\n\n')[1:]]


def one():
    # 1. draw numbers one by one
    # 2. mark each on boards
    # 3. after 5 check if there is a winning board (row or column contains only marked numbers)
    # 4. calculate score of the board
    #    1. find the sum of all unmarked numbers
    #    2. multiply sum by the number that was just called when the board won
    # 5. think about which board will win first
    pass


def two():
    pass

if __name__ == '__main__':
    numbers, boards = _parse_input("04_example.txt")

    for part in [one, two]:
        print(f'Part {part.__name__}: {part(_parse_input("04_example.txt"))}')
