def _parse_input_to_rows(input_filename: str) -> list:
    rows = []
    with open(input_filename, "r") as file_in:
        for ln, line in enumerate(file_in):
            try:
                rows[ln]
            except IndexError:
                rows.append([])
            for bit in line:
                if bit == '\n':
                    continue
                rows[ln].append(int(bit))
    return rows


def filter_numbers(numbers: list, position: int, bit: int) -> list:
    if not type(numbers[0]) == list:
        return numbers

    filtered = []
    for number in numbers:
        if number[position] == bit:
            filtered.append(number)

    return filtered


def get_sum_in_position(numbers: list, position: int) -> int:
    sum = 0
    for number in numbers:
        sum = sum + number[position]
    return sum


def calculate_rating(numbers: list, bit: int) -> int:
    col_num = 0
    while len(numbers) > 1:
        oxygen_generator_sum = get_sum_in_position(numbers, col_num)
        if oxygen_generator_sum >= len(numbers)/2:
            numbers = filter_numbers(numbers, col_num, abs(bit))
        else:
            numbers = filter_numbers(numbers, col_num, abs(bit - 1))
        col_num = col_num + 1

    return int(''.join(str(i) for i in numbers[0]), 2)


# it is is still O(n2)
def one(numbers: list) -> int:
    gamma_rate_bits = []
    epsilon_rate_bits = []

    for col_num in range(len(numbers[0])):
        if get_sum_in_position(numbers, col_num) >= len(numbers)/2:
            gamma_rate_bits.append('1')
            epsilon_rate_bits.append('0')
        else:
            gamma_rate_bits.append('0')
            epsilon_rate_bits.append('1')

    return int(''.join(gamma_rate_bits), 2) * int(''.join(epsilon_rate_bits), 2)


def two(numbers: list) -> int:
    return calculate_rating(numbers, 1) * calculate_rating(numbers, 0)


if __name__ == '__main__':
    rows = _parse_input_to_rows('03_input.txt')

    for part in [one, two]:
        print(f'Part {part.__name__}: {part(rows)}')
