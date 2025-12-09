from typing import List, Tuple
from aoc import read_file

def get_data() -> List[Tuple[int, int]]:
    return [(-1 if line[0] == 'L' else 1, int(line[1:])) for line in read_file(1)]

def solve_part_1(data) -> int:
    x = 50
    count = 0
    for d, n in data:
        x = (x + d * n) % 100
        if x == 0:
            count += 1
    return count

def solve_part_2(data) -> int:
    p = 50
    hits = 0
    for d, n in data:
        q = p + d * n
        h = 1 if q <= 0 and p != 0 else 0
        h += abs(q) // 100
        # print(p, d, n, q, h)
        q %= 100
        hits += h
        p = q
    return hits

if __name__ == "__main__":
    data = get_data()
    print(solve_part_1(data))
    print(solve_part_2(data))
