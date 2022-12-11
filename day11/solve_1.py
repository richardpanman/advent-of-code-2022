from dataclasses import dataclass
import re


def read_file(*, filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as the_file:
        return the_file.read()


@dataclass
class Monkey:
    items: list[int]
    operation: tuple[str, int]
    test_divisible_by: int
    target_if_true: int
    target_if_false: int
    worry_level_divider: int
    inspections: int = 0
    mega_modulo = 1

    OLD = -999999999999

    def take_turn(self) -> list[tuple[int, int]]:
        """tuple is monkey, worry_level"""
        return [
            self.which_monkey_gets_the_item(self.items.pop(0))
            for _ in range(len(self.items))
        ]

    def _calculate_new_worry_level(self, *, worry_level: int) -> int:
        self.inspections += 1
        operand_number = (
            worry_level if self.operation[1] == Monkey.OLD else self.operation[1]
        )
        worry_level = worry_level % self.mega_modulo
        if self.operation[0] == "+":
            return worry_level + operand_number
        return worry_level * operand_number

    def which_monkey_gets_the_item(self, worry_level: int) -> tuple[int, int]:
        """tuple is monkey, worry_level"""
        worry_level = self._calculate_new_worry_level(worry_level=worry_level)
        if self.worry_level_divider != 1:
            worry_level = int(worry_level / self.worry_level_divider)
        if worry_level % self.test_divisible_by == 0:
            return (self.target_if_true, worry_level)
        return (self.target_if_false, worry_level)


def get_numbers_from_string(the_input: str) -> list[int]:
    return list(map(int, re.findall(r"(\d+)", the_input)))


def get_operation_from_string(the_input: str) -> str:
    return str(re.findall(r"\s([\*\+])\s", the_input)[0])


def create_monkeys(*, puzzle_input: str, worry_level_divider: int) -> list[Monkey]:
    monkeys = []
    for description in puzzle_input.split("\n\n"):
        description_lines = description.split("\n")
        monkeys.append(
            Monkey(
                items=get_numbers_from_string(description_lines[1]),
                operation=(
                    get_operation_from_string(description_lines[2]),
                    get_numbers_from_string(description_lines[2])[0]
                    if get_numbers_from_string(description_lines[2])
                    else Monkey.OLD,
                ),
                test_divisible_by=get_numbers_from_string(description_lines[3])[0],
                target_if_true=get_numbers_from_string(description_lines[4])[0],
                target_if_false=get_numbers_from_string(description_lines[5])[0],
                worry_level_divider=worry_level_divider,
            )
        )
    return monkeys


def set_mega_modulo(monkeys: list[Monkey]) -> None:
    mega_modulo = 1
    for monkey in monkeys:
        mega_modulo *= monkey.test_divisible_by
    for monkey in monkeys:
        monkey.mega_modulo = mega_modulo


def solve(*, filename: str, worry_divider: int = 3, turns: int = 20) -> int:
    file_contents = read_file(filename=filename)
    monkeys = create_monkeys(
        puzzle_input=file_contents, worry_level_divider=worry_divider
    )
    set_mega_modulo(monkeys)
    for _ in range(turns):
        for monkey in monkeys:
            thrown_items = monkey.take_turn()
            for item in thrown_items:
                monkeys[item[0]].items.append(item[1])
    top_results = sorted([monkey.inspections for monkey in monkeys], reverse=True)[:2]
    return top_results[0] * top_results[1]


if __name__ == "__main__":
    assert solve(filename="day11/test_input.txt") == 10605
    assert solve(filename="day11/puzzle_input.txt") == 120056
    assert (
        solve(filename="day11/test_input.txt", worry_divider=1, turns=10000)
        == 2713310158
    )
    assert (
        solve(filename="day11/puzzle_input.txt", worry_divider=1, turns=10000)
        == 21816744824
    )
