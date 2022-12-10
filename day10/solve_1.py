def read_file(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as the_file:
        return the_file.read().split("\n")[:-1]


def separate_commands_and_args(lines: list[str]) -> list[tuple]:
    return [tuple(entry.split(" ")) for entry in lines]


def run_commands(commands: list[tuple]) -> list[int]:
    x_register_values = [1]

    for command in commands:
        x_register_values.append(x_register_values[-1])
        if command[0] != "noop":
            x_register_values.append(x_register_values[-1] + int(command[1]))
    return x_register_values


def calculate_power(x_reg_over_time: list[int]) -> int:
    return sum(x_reg_over_time[i - 1] * i for i in range(20, len(x_reg_over_time), 40))


def render_screen(x_reg_over_time: list[int]) -> None:
    for row in range(0, 240, 40):
        print(
            "".join(
                [
                    pixel_value(pixel, x_reg_over_time[row + pixel])
                    for pixel in range(39)
                ]
            )
        )


def pixel_value(pixel: int, sprite_position: int):
    if pixel in [sprite_position, sprite_position - 1, sprite_position + 1]:
        return "#"
    return " "


def solve(filename: str, render: bool = False) -> int:
    command_lines = read_file(filename=filename)
    commands = separate_commands_and_args(lines=command_lines)
    x_reg_over_time = run_commands(commands=commands)
    if render:
        render_screen(x_reg_over_time=x_reg_over_time)
    return calculate_power(x_reg_over_time=x_reg_over_time)


if __name__ == "__main__":
    assert solve("day10/test_input_2.txt") == 13140
    assert solve("day10/puzzle_input_1.txt", render=True) == 15020
