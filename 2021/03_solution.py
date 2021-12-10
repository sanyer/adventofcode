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


def one(numbers: list) -> int:
    gamma_rate_bits = []
    epsilon_rate_bits = []
    row_len = len(numbers[0])
    col_len = len(numbers)

    sums = []
    for bit_num in range(row_len):
        for number in numbers:
            try:
                sums[bit_num]
            except IndexError:
                sums.append(0)
            sums[bit_num] = sums[bit_num] + number[bit_num]

    for _sum in sums:
        if _sum > col_len/2:  # more 1 bits
            gamma_rate_bits.append('1')
            epsilon_rate_bits.append('0')
        else:  # more 0 bits
            gamma_rate_bits.append('0')
            epsilon_rate_bits.append('1')

    gamma_rate = int(''.join(gamma_rate_bits), 2)
    epsilon_rate = int(''.join(epsilon_rate_bits), 2)

    return gamma_rate * epsilon_rate


def two(columns: list) -> int:
    pass


if __name__ == "__main__":
    rows = _parse_input_to_rows("03_example.txt")
    print(f"rows: {rows}")

    for part in [one, two]:
        print(f"Part {part.__name__}: {part(rows)}")
