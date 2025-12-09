from typing import List, Tuple
from aoc import read_file

def get_data() -> List[List[str]]:
    return [[c for c in line.strip()] for line in read_file(7)]

def solve(data: List[List[str]]) -> Tuple[int, int]:
    M, N = len(data), len(data[0])

    # Use DP to find the number of paths going through each cell
    paths = [[0] * N for _ in range(M)]

    # Init
    paths[0][data[0].index('S')] = 1

    # Recursion
    splits = 0
    for y in range(0, M - 1):
        for x in range(N):
            p = paths[y][x]
            if p > 0:
                if data[y + 1][x] == '^':
                    splits += 1
                    if x - 1 >= 0 and data[y + 1][x - 1] == '.': paths[y + 1][x - 1] += p
                    if x + 1 < N and data[y + 1][x + 1] == '.': paths[y + 1][x + 1] += p
                elif data[y + 1][x] == '.':
                    paths[y + 1][x] += p
                else:
                    raise ValueError(x, y, data[y + 1][x], 'must be ^ or .')

    return splits, sum(paths[-1])

if __name__ == "__main__":
    data = get_data()
    print(solve(data))