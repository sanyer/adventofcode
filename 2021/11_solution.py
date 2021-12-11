# https://adventofcode.com/2021/day/11

from pprint import pprint

def _parse_input_to_rows(input_filename: str) -> list:
    with open(input_filename, "r") as fp:
        lines = [line.strip() for line in fp.readlines()]
    return [[int(number) for number in line] for line in lines]


def flash(rows: list, base_pos: int, flash_count: int) -> list:
    rows[base_pos[0]][base_pos[1]] = 0
    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    for direction in directions:
        try:
            posx, posy = base_pos[0] + direction[0], base_pos[1] + direction[1]
            if not rows[posx][posy] == 0:
                rows[posx][posy] += 1
            if not rows[posx][posy] == 0 and rows[posx][posy] > 9:
                flash_count += 1
                rows[posx][posy] = 0
                rows, flash_count = flash(rows, [posx, posy], flash_count)
        except IndexError:
            pass
    return rows, flash_count


def step(rows: list, flash_count: int) -> list:
    # phase 1
    for i, row in enumerate(rows):
        for j, _ in enumerate(row):
            rows[i][j] += 1

    # phase 2
    for i, row in enumerate(rows):
        for j, _ in enumerate(row):
            if rows[i][j] > 9:  # flash
                rows, flash_count = flash(rows, [i, j], flash_count)

    pprint(rows)
    return rows, flash_count


def one(octopuses: list) -> list:
    flash_count = 0
    for _ in range(2):
        octopuses, flash_count = step(octopuses, flash_count)
    return flash_count


def two(octopuses: list) -> list:
    pass


if __name__ == '__main__':
    rows = _parse_input_to_rows('11_example.txt')

    for part in [one, two]:
        print(f'Part {part.__name__}: {part(rows)}')
