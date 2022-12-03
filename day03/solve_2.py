"""Advent of Code 2022 - day 3 - problem 2"""

priority_score_for_item = {chr(code): code - 96 for code in range(97, 123)}
for code in range(65, 91):
    priority_score_for_item[chr(code)] = code - 64 + 26


def solve() -> int:
    """Solve the puzzle"""
    all_rucksacks = read_all_rucksacks_from_file(filename="day03/puzzle_input.txt")
    common_items = get_all_the_common_items(all_rucksacks=all_rucksacks)
    return calculate_the_score(common_items=common_items)


def read_all_rucksacks_from_file(*, filename: str) -> list[str]:
    """Read all the rucksacks from file"""
    with open(filename, "r", encoding="utf-8") as rucksack:
        return rucksack.read().splitlines()


def get_all_the_common_items(*, all_rucksacks) -> list[str]:
    """Calculate the score"""
    return [
        find_common_item_in_elf_team_rucksacks(rucksacks=elf_team_rucksacks)
        for elf_team_rucksacks in elf_team_rucksack_distributor(
            rucksacks=all_rucksacks, elf_team_size=3
        )
    ]


def find_common_item_in_elf_team_rucksacks(*, rucksacks: list) -> str:
    """Find the common item in all the rucksacks"""
    the_set = {*rucksacks[0]}
    for rucksack in rucksacks[1:]:
        the_set = the_set & {*rucksack}
    return list(the_set)[0]


def elf_team_rucksack_distributor(*, rucksacks: list, elf_team_size: int) -> list:
    """Distribute the rucksacks across teams of the given size"""
    for start_rucksack in range(0, len(rucksacks), elf_team_size):
        yield rucksacks[start_rucksack : start_rucksack + elf_team_size]


def calculate_the_score(*, common_items: list[str]) -> int:
    """Return the sum of the priority score for the provided items"""
    return sum(priority_score_for_item[item] for item in common_items)


if __name__ == "__main__":
    print(solve())
