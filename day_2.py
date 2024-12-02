INPUT_FILE = 'input.txt'

def load_input_lines(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().splitlines()

def check_differences(numbers: list[int]) -> bool:
    return all(0 < b - a < 4 for a, b in zip(numbers, numbers[1:]))

def is_safe(row: list[int]) -> bool:
    return check_differences(row) or check_differences(row[::-1])

def is_safe_with_one_removed(row: list[int]) -> bool:
    if is_safe(row):
        return True
    return any(is_safe(row[:i] + row[i + 1:]) for i in range(len(row)))

def solve_part_1(file_path: str = INPUT_FILE) -> int:
    return sum(
        is_safe([int(n) for n in line.split()])
        for line in load_input_lines(file_path)
    )

def solve_part_2(file_path: str = INPUT_FILE) -> int:
    return sum(
        is_safe_with_one_removed([int(n) for n in line.split()])
        for line in load_input_lines(file_path)
    )

print(solve_part_1())
print(solve_part_2())
