def get_log_entries(filename: str) -> list[str]:
    with open(filename, "r", encoding="utf-8") as terminal_log:
        return [entry.split("\n")[:-1] for entry in terminal_log.read().split("$ ")[1:]]


def change_directory(current_dir: str, command_parameter: str) -> str:
    if command_parameter.startswith("/"):
        return command_parameter
    if command_parameter == "..":
        new_directory = "/".join(current_dir.split("/")[:-1])
        return new_directory or "/"
    if current_dir == "/":
        return f"/{command_parameter}"
    return f"{current_dir}/{command_parameter}"


def get_directory_size(ls_lines: list[str]) -> int:
    return sum(
        int(ls_line.split(" ")[0])
        for ls_line in ls_lines
        if not ls_line.startswith("dir ")
    )


log_entries = get_log_entries("day07/puzzle_input.txt")
print(f"{log_entries=}")
current_directory = ""
individual_directory_sizes = {}
for entry in log_entries:
    if entry[0].startswith("cd"):
        current_directory = change_directory(
            current_dir=current_directory, command_parameter=entry[0].split(" ")[1]
        )
        print(f"{current_directory=}")
    if entry[0].startswith("ls"):
        dir_size = get_directory_size(entry[1:])
        if current_directory not in individual_directory_sizes:
            individual_directory_sizes[current_directory] = dir_size

print(individual_directory_sizes)
directory_size_with_subdirs = {
    directory: sum(
        value
        for key, value in individual_directory_sizes.items()
        if key.startswith(directory)
    )
    for directory in individual_directory_sizes
}

print(directory_size_with_subdirs)

print(
    sum(
        directory_size
        for directory_size in directory_size_with_subdirs.values()
        if directory_size <= 100000
    )
)

# answer 1 = 1141028

total_disk_space = 70000000
space_in_use = directory_size_with_subdirs["/"]
print(f"{space_in_use=}")
unused_space = total_disk_space - space_in_use
print(f"{unused_space=}")
space_needed = 30000000
space_to_be_freed = space_needed - unused_space
print(f"{space_to_be_freed=}")

directory_to_delete = "/"
selected_dir_size = total_disk_space
for directory, directory_size in directory_size_with_subdirs.items():
    if directory_size < selected_dir_size and directory_size > space_to_be_freed:
        directory_to_delete = directory
        selected_dir_size = directory_size
print(directory_to_delete, selected_dir_size)

# 7999160 too low
