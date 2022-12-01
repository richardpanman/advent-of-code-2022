def solve() -> int:
    
    with open("day01/puzzle_input.txt", "r", encoding="utf-8") as example:
        most_calories_carried = 0
        running_total = 0
        while line := example.readline():
            if line.isspace():
                if running_total>=most_calories_carried:
                    most_calories_carried=running_total
                running_total = 0
            else:
                running_total+=int(line.strip())
        return most_calories_carried
    
if __name__ == "__main__":
    print(solve())