from typing import List, Tuple
from itertools import chain
from aoc import read_file

def get_data() -> Tuple[List[Tuple[int, int]], List[int]]:
    lines = read_file(5)
    div = lines.index('\n')
    ranges = [(int(i), int(j)) for [i, j] in (line.split('-') for line in lines[:div])]
    ingredients = [int(i) for i in lines[div + 1:]]
    return ranges, ingredients

def solve_part_1(data):
    ranges, ingredients = data
    return sum(any(i <= ingredient <= j for i, j in ranges) for ingredient in ingredients)

def solve_part_2(data):
    ranges, _ = data
    # Merge the ranges
    sorted_ranges = list(sorted(ranges))
    new_ranges = [sorted_ranges[0]]
    for i, j in sorted_ranges[1:]:
        lb, ub = new_ranges[-1]
        if i <= ub:
            new_ranges[-1] = lb, max(ub, j)
        else:
            new_ranges.append((i, j))
    # Sum the lengths of the ranges
    return sum(j - i + 1 for i, j in new_ranges)

if __name__ == "__main__":
    data = get_data()
    print(solve_part_1(data))
    print(solve_part_2(data))
