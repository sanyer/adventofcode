# https://adventofcode.com/2021/day/11


def _parse_input_to_rows(input_filename: str) -> list:
    with open(input_filename, "r") as fp:
        lines = [line.strip() for line in fp.readlines()]
    return [[int(number) for number in line] for line in lines]


def flash(flash_table: list, base_pos: int, flash_count: int) -> list:
    flash_count += 1
    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
    for direction in directions:
        try:
            posx, posy = base_pos[0] + direction[0], base_pos[1] + direction[1]
            if posx < 0 or posy < 0 or flash_table[posx][posy] == 0:
                raise IndexError
            flash_table[posx][posy] += 1
        except IndexError:
            pass
    flash_table[base_pos[0]][base_pos[1]] = 0
    return flash_table, flash_count


def step(temp_table: list, flash_count: int) -> list:
    flash_exists = False
    for i, row in enumerate(temp_table):
        for j, _ in enumerate(row):
            temp_table[i][j] += 1
            if temp_table[i][j] > 9:  # flash
                flash_exists = True

    while flash_exists:
        flash_exists = False
        for i, row in enumerate(temp_table):
            for j, _ in enumerate(row):
                if temp_table[i][j] > 9:  # flash
                    flash_exists = True
                    temp_table, flash_count = flash(temp_table, [i, j], flash_count)
    return temp_table, flash_count


def one(one_input: list) -> list:
    flash_count = 0
    for _ in range(100):
        one_input, flash_count = step(one_input, flash_count)
    return flash_count


def two(two_input: list) -> list:
    all_flash = False
    all_flash_step = 0
    while not all_flash:
        two_input, _ = step(two_input, 0)
        all_flash_step += 1
        row_sum  = sum([sum(row) for row in two_input])
        if row_sum == 0:
            all_flash = True
    return all_flash_step


if __name__ == '__main__':
    for part in [one, two]:
        print(f'Part {part.__name__}: {part(_parse_input_to_rows("11_input.txt"))}')
