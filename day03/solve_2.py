"""Advent of Code 2022 - day 3 - problem 2"""

priority_score_for_item = {chr(code): code - 96 for code in range(97, 123)}
for code in range(65, 91):
    priority_score_for_item[chr(code)] = code - 64 + 26


def elf_team_rucksack_distributor(*, rucksacks: list, elf_team_size: int) -> list:
    """Distribute the rucksacks across teams of the given size"""
    for start_rucksack in range(0, len(rucksacks), elf_team_size):
        yield rucksacks[start_rucksack : start_rucksack + elf_team_size]


def find_common_item_in_elf_team_rucksacks(*, rucksacks: list) -> str:
    """Find the common item in all the rucksacks"""
    the_set = {*rucksacks[0]}
    for rucksack in rucksacks[1:]:
        the_set = the_set & {*rucksack}
    return list(the_set)[0]


def solve() -> int:
    """Solve the puzzle"""
    with open("day03/puzzle_input.txt", "r", encoding="utf-8") as rucksack:
        all_rucksacks = rucksack.read().splitlines()
    sum_of_priorities = 0
    for elf_team_rucksacks in elf_team_rucksack_distributor(
        rucksacks=all_rucksacks, elf_team_size=3
    ):
        common_item = find_common_item_in_elf_team_rucksacks(
            rucksacks=elf_team_rucksacks
        )
        sum_of_priorities += priority_score_for_item[common_item]
    return sum_of_priorities


if __name__ == "__main__":
    print(solve())
