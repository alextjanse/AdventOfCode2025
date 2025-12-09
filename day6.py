from typing import List, Tuple
from operator import mul, add
from functools import reduce
from itertools import takewhile
from aoc import read_file

def get_data() -> Tuple[List[List[int]], List[str]]:
    lines = read_file(6)
    nums = [[int(c) for c in line.split()] for line in lines[:-1]]
    ops = lines[-1].split()
    return nums, ops

def solve_part_1(data):
    nums, ops = data
    total = 0
    for i, op in enumerate(ops):
        if op == '*':
            total += reduce(mul, (num[i] for num in nums), 1)
        elif op == '+':
            total += reduce(add, (num[i] for num in nums), 0)
        else:
            raise ValueError(op, 'must be + or *')
    return total

def solve_part_2(data):
    lines = read_file(6)
    transposed = [''.join([lines[y][x] for y in range(len(lines) - 1)]).strip() for x in range(len(lines[-1]))]
    ops = lines[-1].split()
    total = 0
    for op in ops:
        nums = [int(n) for n in takewhile(lambda l: l != '', transposed)]
        if op == '*':
            total += reduce(mul, nums, 1)
        elif op == '+':
            total += reduce(add, nums, 0)
        transposed = transposed[len(nums) + 1:]
    return total

if __name__ == "__main__":
    data = get_data()
    print(solve_part_1(data))
    print(solve_part_2(data))
