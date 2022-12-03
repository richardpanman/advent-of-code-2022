def solve() -> int:
    total = 0
    # A for Rock, B for Paper, and C for Scissors
    # X for Rock, Y for Paper, and Z for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    # shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    score_map = {
        "A X": 3 + 1,
        "A Y": 6 + 2,
        "A Z": 0 + 3,
        "B X": 0 + 1,
        "B Y": 3 + 2,
        "B Z": 6 + 3,
        "C X": 6 + 1,
        "C Y": 0 + 2,
        "C Z": 3 + 3,
    }

    with open("day02/puzzle_input.txt", "r", encoding="utf-8") as input_file:
        while line := input_file.readline():
            total += int(score_map[line.strip()])
    return total


if __name__ == "__main__":
    print(solve())
