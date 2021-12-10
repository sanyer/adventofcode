def _parse_input(input_filename: str) -> list:
    lines = []
    with open(input_filename, "r") as file_in:
        for line in file_in:
            lines.append(int(line))
    return lines


def one(measurements: list) -> int:
    increases = 0
    previous_measurement = 1e9

    for measurement in measurements:
        if measurement > previous_measurement:
            increases = increases + 1
        previous_measurement = measurement

    return increases


def two(measurements: list) -> int:
    sliding_sums = []

    for index, _ in enumerate(measurements):
        try:
            measurements[index+2]
        except IndexError:
            break
        else:
            sliding_sums.append(sum(measurements[index:index+3]))

    return one(sliding_sums)


if __name__ == "__main__":
    measurements = _parse_input("01_input.txt")
    for part in [one, two]:
        print(f"Part {part.__name__}: {part(measurements)}")
