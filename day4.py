from typing import List, Set, Tuple
from aoc import read_file

def get_data() -> Set[Tuple[int, int]]:
    rolls = set()
    for y, line in enumerate(read_file(4)):
        for x, c in enumerate(line):
            if c == '@':
                rolls.add((x, y))
    return rolls

def get_nbs(x, y, rolls) -> int:
    nbs = -1
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if (x + dx, y + dy) in rolls:
                # dx = 0, dy = 0 will hit, so nbs = -1 at init
                nbs += 1
    return nbs

def solve_part_1(rolls) -> int:
    total = 0

    for x, y in rolls:
        nbs = get_nbs(x, y, rolls)
        if nbs < 4:
            total += 1

    return total

def solve_part_2(rolls) -> int:
    total = 0

    prev_rolls = set(rolls)
    next_rolls = { (x, y) for (x, y) in rolls if get_nbs(x, y, prev_rolls) >= 4 }
    while len(next_rolls) < len(prev_rolls):
        total += len(prev_rolls) - len(next_rolls)
        prev_rolls = next_rolls
        next_rolls = { (x, y) for (x, y) in rolls if get_nbs(x, y, prev_rolls) >= 4 }

    return total

if __name__ == "__main__":
    data = get_data()
    print(solve_part_1(data))
    print(solve_part_2(data))
