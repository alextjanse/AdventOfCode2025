from typing import List
from aoc import read_file

def get_data() -> List[List[int]]:
    return [[int(c) for c in line.strip()] for line in read_file(3)]

def solve_part_1(data) -> int:
    total = 0
    for bank in data:
        a = max(range(0, len(bank) - 1), key=lambda i: bank[i])
        b = max(range(a + 1, len(bank)), key=lambda i: bank[i])
        j = 10 * bank[a] + bank[b]
        total += j
    return total

def solve_part_2(data) -> int:
    total = 0
    for bank in data:
        l = len(bank)
        nums = []
        i = 0
        while len(nums) < 12:
            j = max(range(i, l - 12 + len(nums) + 1), key=lambda i: bank[i])
            nums.append(bank[j])
            i = j + 1
        joltage = 0
        for n in nums:
            joltage = joltage * 10 + n
        total += joltage
    return total

if __name__ == "__main__":
    data = get_data()
    print(solve_part_1(data))
    print(solve_part_2(data))
