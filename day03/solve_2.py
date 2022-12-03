def get_matching_letter(str1: list[str], str2: list[str]) -> str:
    return list(set(str1) & set(str2))[0]


priorities = {chr(code): code - 96 for code in range(97, 123)}
for code in range(65, 91):
    priorities[chr(code)] = code - 64 + 26


def split_sucksacks_into_elf_teams(rucksacks: list, elf_team_size: int) -> list:
    for start_rucksack in range(0, len(rucksacks), elf_team_size):
        yield rucksacks[start_rucksack : start_rucksack + elf_team_size]


def find_common_item_in_elf_team_rucksacks(rucksacks: list) -> str:
    the_set = {*rucksacks[0]}
    for rucksack in rucksacks[1:]:
        the_set = the_set & {*rucksack}
    return list(the_set)[0]


def solve() -> int:
    with open("day03/puzzle_input.txt", "r", encoding="utf-8") as rucksack:
        all_rucksacks = rucksack.read().splitlines()
    sum_of_priorities = 0
    elf_teams = split_sucksacks_into_elf_teams(all_rucksacks, 3)
    for elf_team_rucksacks in elf_teams:
        common_item = find_common_item_in_elf_team_rucksacks(elf_team_rucksacks)
        sum_of_priorities += priorities[common_item]
    return sum_of_priorities


if __name__ == "__main__":
    print(solve())
