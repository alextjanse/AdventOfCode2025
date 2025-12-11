from typing import List, Set, Tuple
from aoc import read_file

def get_data() -> List[Tuple[int, int]]:
    data: List[Tuple[int, int]] = []
    for line in read_file(9):
        [x, y] = [int(i) for i in line.split(',', 1)]
        data.append((x, y))
    return data

def solve_part_1(data):
    max_rect = 0
    for x_i, y_i in data[:-1]:
        for x_j, y_j in data[1:]:
            dx = abs(x_i - x_j) + 1
            dy = abs(y_i - y_j) + 1
            max_rect = max(dx * dy, max_rect)
    return max_rect

def solve_part_2(data):
    # Sort the line segments, s.t. a < b for all line segments
    line_segments = [(a, b) if a < b else (b, a) for a, b in zip(data, data[1:] + data[:1])]
    max_rect = 0
    for i, (x_i, y_i) in enumerate(data):
        for x_j, y_j in data[i + 1:]:
            [x_min, x_max] = sorted([x_i, x_j])
            [y_min, y_max] = sorted([y_i, y_j])
            # Check if any line segment intersects with the rectangle
            if not any(x_a < x_max and x_b > x_min and y_a < y_max and y_b > y_min for ((x_a, y_a), (x_b, y_b)) in line_segments):
                rect = (x_max - x_min + 1) * (y_max - y_min + 1)
                max_rect = max(max_rect, rect)
    return max_rect

if __name__ == "__main__":
    data = get_data()
    print(solve_part_1(data))
    print(solve_part_2(data))
