# https://adventofcode.com/2021/day/2

def _parse_input(input_filename: str) -> list:
    lines = []
    with open(input_filename, "r") as file_in:
        for line in file_in:
            lines.append(tuple(line.split()))
    return lines


def one(commands: list) -> int:
    horizontal_position = 0
    depth = 0

    for command in commands:
        if command[0] == 'forward':
            horizontal_position = horizontal_position + int(command[1])
        elif command[0] == 'down':
            depth = depth + int(command[1])
        elif command[0] == 'up':
            depth = depth - int(command[1])

    return horizontal_position * depth


def two(commands: list) -> int:
    horizontal_position = 0
    depth = 0
    aim = 0

    for command in commands:
        if command[0] == 'forward':
            horizontal_position = horizontal_position + int(command[1])
            depth = depth + aim*int(command[1])
        elif command[0] == 'down':
            aim = aim + int(command[1])
        elif command[0] == 'up':
            aim = aim - int(command[1])

    return horizontal_position * depth


if __name__ == "__main__":
    commands = _parse_input("02_input.txt")
    for part in [one, two]:
        print(f"Part {part.__name__}: {part(commands)}")
