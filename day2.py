from typing import List, Tuple
from aoc import read_file

def get_data() -> List[Tuple[int, int]]:
    data: List[Tuple[int, int]] = []
    for line in read_file(2):
        for pair in line.split(','):
            [x, y] = pair.split('-')
            data.append((int(x), int(y)))
    return data

def check_1(id: int) -> bool:
    s = str(id)
    l = len(s)
    m = l // 2
    return l % 2 == 0 and s[:m] == s[m:]

def solve_part_one(data) -> int:
    total = 0
    for x, y in data:
        i = x
        while i <= y:
            if check_1(i):
                total += i
            i += 1
    return total

def check_2(id: int) -> bool:
    s = str(id)
    l = len(s)
    i = 1
    while i <= l // 2:
        if l % i == 0:
            q = s[:i]
            if all(s[i * j: i * j + i] == q for j in range(0, l // i)):
                return True
        i += 1
    return False

def solve_part_two(data) -> int:
    total = 0
    for x, y in data:
        i = x
        while i <= y:
            if check_2(i):
                total += i
            i += 1
    return total

if __name__ == "__main__":
    data = get_data()
    print(solve_part_one(data))
    print(solve_part_two(data))
