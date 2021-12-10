def _parse_input_to_columns(input_filename: str) -> list:
    columns = []
    with open(input_filename, "r") as file_in:
        for line in file_in:
            for bn, bit in enumerate(line):
                if bit == '\n':
                    continue

                try:
                    columns[bn]
                except IndexError:
                    columns.append([])

                columns[bn].append(int(bit))

    return columns

def one(columns: list) -> int:
    sums = []
    for bit in columns:
        sums.append(sum(bit))

    gamma_rate_bits = []
    epsilon_rate_bits = []
    column_length = len(columns[0])
    for _sum in sums:
        if _sum > column_length/2:
            gamma_rate_bits.append('1')
            epsilon_rate_bits.append('0')
        else:
            gamma_rate_bits.append('0')
            epsilon_rate_bits.append('1')

    gamma_rate = int(''.join(gamma_rate_bits), 2)
    epsilon_rate = int(''.join(epsilon_rate_bits), 2)

    return gamma_rate * epsilon_rate

def two(columns: list) -> int:
    pass


if __name__ == "__main__":
    columns = _parse_input_to_columns("03_input.txt")
    for part in [one, two]:
        print(f"Part {part.__name__}: {part(columns)}")
