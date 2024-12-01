from collections import Counter

INPUT_FILE = 'input.txt'

def load_input_lines(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return file.read().splitlines()
    
def parse_number_pairs(lines: list[str]) -> tuple[list[int], list[int]]:
    numbers = [[int(n) for n in line.split() if n.isdigit()] for line in lines]
    return list(zip(*numbers))

def solve_part_1(file_path: str = INPUT_FILE) -> int:
    left, right = parse_number_pairs(load_input_lines(file_path))
    return sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))

def solve_part_2(file_path: str = INPUT_FILE) -> int:
    left, right = parse_number_pairs(load_input_lines(file_path))
    frequency = Counter(right)
    return sum(x * frequency.get(x, 0) for x in left)

print(solve_part_1())
print(solve_part_2())
