def read_file(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as tree_file:
        return tree_file.read().split("\n")[:-1]


def move_h_sprite(sprite: list[int], direction: str) -> list[int]:
    if direction == "L":
        return [sprite[0] - 1, sprite[1]]
    if direction == "R":
        return [sprite[0] + 1, sprite[1]]
    if direction == "U":
        return [sprite[0], sprite[1] + 1]
    return [sprite[0], sprite[1] - 1]


def move_following_sprite(
    lead_sprite: list[int], following_sprite: list[int]
) -> list[int]:
    if (
        abs(lead_sprite[0] - following_sprite[0]) <= 1
        and abs(lead_sprite[1] - following_sprite[1]) <= 1
    ):
        return following_sprite
    return [
        following_sprite[0] + max(min(1, lead_sprite[0] - following_sprite[0]), -1),
        following_sprite[1] + max(min(1, lead_sprite[1] - following_sprite[1]), -1),
    ]


def solve() -> int:
    moves = get_moves_from_file("day09/puzzle_input.txt")

    head_sprite = [0, 0]
    t_sprite = [0, 0]
    tail_sprite_visited_positions = set()
    for move in moves:
        for _x in range(int(move[1])):
            head_sprite = move_h_sprite(head_sprite, move[0])
            t_sprite = move_following_sprite(
                lead_sprite=head_sprite, following_sprite=t_sprite
            )
            tail_sprite_visited_positions.add(
                "_".join([str(position) for position in t_sprite])
            )
    return len(tail_sprite_visited_positions)


def get_moves_from_file(filename: str) -> list[list[str]]:
    move_input = read_file(filename)
    return [move.split(" ") for move in move_input]


assert solve() == 6026
