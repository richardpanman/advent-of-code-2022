import re


def get_stack_and_instruction_lines(filename: str) -> tuple[list[str], list[str]]:
    with open(filename, "r", encoding="utf-8") as the_file:
        return_stack_lines = []
        return_instruction_lines = []
        reading_the_stack = True

        all_lines = the_file.readlines()
        for line in all_lines:
            line = line.replace("\n", "")
            if line == "":
                reading_the_stack = False
                continue
            if reading_the_stack:
                return_stack_lines.append(line)
                continue
            return_instruction_lines.append(line)
    return return_stack_lines, return_instruction_lines


def convert_stack_lines_to_stacks(input_stack_lines: list[str]) -> list[list[str]]:
    input_stack_lines = input_stack_lines[:-1]
    input_stack_lines = [re.findall(r".(.).\s?", stack) for stack in input_stack_lines]
    input_stack_lines.reverse()  # get the right stack on the bottom
    return_stacks = [list(entry) for entry in zip(*input_stack_lines)]
    for idx, item in enumerate(return_stacks):
        return_stacks[idx] = [entry for entry in item if entry != " "]
    return return_stacks


def move_crates_one_at_a_time(
    our_stacks: list[list[str]], our_instructions: list[str]
) -> None:
    for instruction in our_instructions:
        items, from_stack, to_stack = interpret_instructions(instruction)
        for _x in range(int(items)):
            crate_that_is_moving = pick_up_single_crate(our_stacks, from_stack)
            put_crate_on_new_stack(our_stacks, to_stack, crate_that_is_moving)


def put_crate_on_new_stack(our_stacks, to_stack, crate_that_is_moving):
    our_stacks[int(to_stack) - 1].append(crate_that_is_moving)


def pick_up_single_crate(our_stacks, from_stack):
    return our_stacks[int(from_stack) - 1].pop()


def move_multiple_crates(
    our_stacks: list[list[str]], our_instructions: list[str]
) -> None:
    for instruction in our_instructions:
        items, from_stack, to_stack = interpret_instructions(instruction)
        crates_that_are_moving = select_crates_to_move(our_stacks, items, from_stack)
        pick_up_the_crates(our_stacks, items, from_stack)
        put_crates_on_new_stack(our_stacks, to_stack, crates_that_are_moving)


def put_crates_on_new_stack(our_stacks, to_stack, crates_that_are_moving):
    our_stacks[int(to_stack) - 1] += crates_that_are_moving


def pick_up_the_crates(our_stacks, items, from_stack):
    our_stacks[int(from_stack) - 1] = our_stacks[int(from_stack) - 1][
        : len(our_stacks[int(from_stack) - 1]) - int(items)
    ]


def select_crates_to_move(our_stacks, items, from_stack):
    return our_stacks[int(from_stack) - 1][
        len(our_stacks[int(from_stack) - 1]) - int(items) :
    ]


def interpret_instructions(instruction):
    items, from_stack, to_stack = re.findall(
        r"move (\d+) from (\d+) to (\d+)", instruction
    )[0]

    return items, from_stack, to_stack


def get_crates_on_top_of_stacks(our_crates: list[list[str]]) -> str:
    return "".join([entry[-1] for entry in our_crates])


def get_answer_for_file(filename: str, moving_function: callable) -> str:
    stack_lines, instruction_lines = get_stack_and_instruction_lines(filename=filename)
    stacks = convert_stack_lines_to_stacks(stack_lines)
    moving_function(stacks, instruction_lines)
    return get_crates_on_top_of_stacks(stacks)


assert get_answer_for_file("day05/test_input.txt", move_crates_one_at_a_time) == "CMZ"
assert (
    get_answer_for_file("day05/puzzle_input.txt", move_crates_one_at_a_time)
    == "TWSGQHNHL"
)

assert (
    get_answer_for_file(
        filename="day05/test_input.txt", moving_function=move_multiple_crates
    )
    == "MCD"
)
assert (
    get_answer_for_file(
        filename="day05/puzzle_input.txt", moving_function=move_multiple_crates
    )
    == "JNRSCDWPP"
)
