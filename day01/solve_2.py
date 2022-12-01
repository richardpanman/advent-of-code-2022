def solve() -> int:
    
    with open("day01/puzzle_input.txt", "r", encoding="utf-8") as example:
        calories_carried = []
        running_total = 0
        while line := example.readline():
            if line.isspace():
                calories_carried.append(running_total)
                running_total = 0
            else:
                running_total+=int(line.strip())
        calories_carried.sort(reverse=True)
        return sum(calories_carried[:3])
    
if __name__ == "__main__":
    print(solve())