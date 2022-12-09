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

    sprites = [[0, 0] for _x in range(10)]

    tail_sprite_visited_positions = set()
    for move in moves:
        for _x in range(int(move[1])):
            sprites[0] = move_h_sprite(sprites[0], move[0])
            for following_sprite_count, following_sprite in enumerate(sprites[1:]):
                sprites[following_sprite_count + 1] = move_following_sprite(
                    lead_sprite=sprites[following_sprite_count],
                    following_sprite=following_sprite,
                )
            tail_sprite_visited_positions.add(
                "_".join([str(position) for position in sprites[9]])
            )
    return len(tail_sprite_visited_positions)


def get_moves_from_file(filename: str) -> list[list[str]]:
    move_input = read_file(filename)
    return [move.split(" ") for move in move_input]


assert solve() == 2273
