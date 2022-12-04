def get_numbers_from_range(the_range: str) -> set[int]:
    return set(range(int(the_range.split("-")[0]), int(the_range.split("-")[1]) + 1))


def get_elf_assignment_pairs(filename: str) -> list[tuple]:
    with open(filename, "r", encoding="utf-8") as the_file:
        pair_assignments = [a.strip().split(",") for a in the_file.readlines()]
        return [
            [
                get_numbers_from_range(pair_assignment[0]),
                get_numbers_from_range(pair_assignment[1]),
            ]
            for pair_assignment in pair_assignments
        ]


def count_all_encompassing_pairs(pairs):
    return sum(
        (
            elf_assignment_pair[0].issubset(elf_assignment_pair[1])
            or elf_assignment_pair[1].issubset(elf_assignment_pair[0])
        )
        for elf_assignment_pair in pairs
    )


if __name__ == "__main__":
    elf_assignment_pairs = get_elf_assignment_pairs("day04/puzzle_input.txt")
    print(count_all_encompassing_pairs(elf_assignment_pairs))
