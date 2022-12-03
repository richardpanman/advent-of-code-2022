def get_matching_letter(str1: list[str], str2: list[str]) -> str:
    return list(set(str1) & set(str2))[0]


priorities = {chr(code): code - 96 for code in range(97, 123)}
for code in range(65, 91):
    priorities[chr(code)] = code - 64 + 26


def solve() -> int:
    with open("day03/puzzle_input.txt", "r", encoding="utf-8") as rucksack:
        sum_of_priorities = 0
        while items := rucksack.readline():
            items = [*items.strip()]
            middle = len(items) // 2
            first_compartment = items[:middle]
            second_compartment = items[middle:]
            matching_item = get_matching_letter(first_compartment, second_compartment)
            sum_of_priorities += priorities[matching_item]
        return sum_of_priorities


if __name__ == "__main__":
    print(solve())
