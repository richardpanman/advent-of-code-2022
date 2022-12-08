def get_tree_rows(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as tree_file:
        return tree_file.read().split("\n")[:-1]


def is_this_central_tree_visible_from_the_edge(
    tree_rows: list[str], row: int, col: int
) -> bool:
    for line_of_sight in [
        tree_rows[row][:col],  # left
        tree_rows[row][col + 1 :],  # right
        "".join(tree[col] for tree in tree_rows[:row]),  # up
        "".join(tree[col] for tree in tree_rows[row + 1 :]),  # down
    ]:
        if all([tree < tree_rows[row][col] for tree in line_of_sight]):
            return True
    return False


def count_visible_trees(tree_rows: list[str]) -> int:
    last_tree_in_row = len(tree_rows[0]) - 1
    visible_trees = 0
    for row_index, tree_row in enumerate(tree_rows):
        for col_index, tree_column in enumerate(tree_row):
            if row_index in [0, len(tree_rows) - 1] or col_index in [
                0,
                last_tree_in_row,
            ]:
                visible_trees += 1
            elif is_this_central_tree_visible_from_the_edge(
                tree_rows=tree_rows, row=row_index, col=col_index
            ):
                visible_trees += 1
    return visible_trees


if __name__ == "__main__":
    trees = get_tree_rows("day08/test_input.txt")
    assert count_visible_trees(trees) == 21
    trees = get_tree_rows("day08/puzzle_input.txt")
    assert count_visible_trees(trees) == 1820
