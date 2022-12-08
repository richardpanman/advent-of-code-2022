def get_tree_rows(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as tree_file:
        return tree_file.read().split("\n")[:-1]


def get_lines_of_sight(tree_rows: list[str], row: int, col: int) -> list[str]:
    return [
        tree_rows[row][:col][::-1],  # left
        tree_rows[row][col + 1 :],  # right
        "".join(tree[col] for tree in tree_rows[:row])[::-1],  # up
        "".join(tree[col] for tree in tree_rows[row + 1 :]),  # down
    ]


def get_best_scenic_score(tree_rows: list[str]) -> int:
    last_tree_in_row = len(tree_rows[0]) - 1
    best_scenic_score = 0
    for row_index, tree_row in enumerate(tree_rows):
        for col_index, _tree_column in enumerate(tree_row):
            if row_index in [0, len(tree_rows) - 1] or col_index in [
                0,
                last_tree_in_row,
            ]:
                continue
            scenic_score = calculate_scenic_score(
                tree_rows,
                row_index,
                col_index,
            )
            if scenic_score > best_scenic_score:
                best_scenic_score = scenic_score
    return best_scenic_score


def get_scenic_multiplier(line_of_sight: str, my_tree_height: str) -> int:
    return next(
        (
            tree_index + 1
            for tree_index, tree_height in enumerate(line_of_sight)
            if int(my_tree_height) <= int(tree_height)
        ),
        len(line_of_sight),
    )


def calculate_scenic_score(tree_rows: list[str], row: str, col: str) -> int:
    scenic_score = 1
    lines_of_sight = get_lines_of_sight(tree_rows, row, col)
    for line_of_sight in lines_of_sight:
        multiplier = get_scenic_multiplier(
            line_of_sight=line_of_sight, my_tree_height=tree_rows[row][col]
        )
        scenic_score *= multiplier
    return scenic_score


if __name__ == "__main__":
    trees = get_tree_rows("day08/puzzle_input.txt")
    assert get_best_scenic_score(trees) == 385112
