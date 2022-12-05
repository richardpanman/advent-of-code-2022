import re


def get_stack_and_instruction_lines():
    with open("day05/puzzle_input.txt", "r", encoding="utf-8") as the_file:
        stack_lines = []
        instruction_lines = []
        READING_STACK = True
        all_lines = the_file.readlines()
        for line in all_lines:
            line = line.replace("\n", "")
            if line == "":
                READING_STACK = False
                continue
            if READING_STACK:
                stack_lines.append(line)
                continue
            instruction_lines.append(line)
    return stack_lines, instruction_lines


def convert_stack_lines_to_stacks(input_stack_lines):
    input_stack_lines = input_stack_lines[:-1]
    input_stack_lines = [re.findall(r".(.).\s?", stack) for stack in input_stack_lines]
    input_stack_lines.reverse()  # get the right stack on the bottom
    return_stacks = [list(entry) for entry in zip(*input_stack_lines)]
    for idx, item in enumerate(return_stacks):
        return_stacks[idx] = [entry for entry in item if entry != " "]
    return return_stacks


def move(our_stacks, our_instructions):
    for instruction in our_instructions:
        items, from_stack, to_stack = re.findall(
            r"move (\d+) from (\d+) to (\d+)", instruction
        )[0]
        for _x in range(int(items)):
            our_stacks[int(to_stack) - 1].append(our_stacks[int(from_stack) - 1].pop())


def answer(our_crates):
    return "".join([entry[-1] for entry in our_crates])


stack_lines, instruction_lines = get_stack_and_instruction_lines()
stacks = convert_stack_lines_to_stacks(stack_lines)
move(stacks, instruction_lines)
print(answer(stacks))
