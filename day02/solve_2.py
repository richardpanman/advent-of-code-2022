
def solve()->int:
    total = 0
    # A for Rock, B for Paper, and C for Scissors
    # X to lose, Y to draw, X to win
    strategy_map = {
        "A X": "A C",
        "A Y": "A A",
        "A Z": "A B",
        "B X": "B A",
        "B Y": "B B",
        "B Z": "B C",
        "C X": "C B",
        "C Y": "C C",
        "C Z": "C A",
    }
    
    # A for Rock, B for Paper, and C for Scissors
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    # shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    score_map = {
        "A A": 3+1,
        "A B": 6+2,
        "A C": 0+3,
        "B A": 0+1,
        "B B": 3+2,
        "B C": 6+3,
        "C A": 6+1,
        "C B": 0+2,
        "C C": 3+3,
    }
    
    with open("day02/puzzle_input.txt", "r", encoding="utf-8") as input_file:
        while line := input_file.readline():
            total+=int(score_map[strategy_map[line.strip()]])
    return total
if __name__ == "__main__":
    print(solve())