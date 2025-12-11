from functools import reduce
from operator import mul
from typing import List, Tuple
from aoc import read_file

type Vec = Tuple[int, int, int]

def get_data() -> List[Vec]:
    data = []
    for line in read_file(8):
        xyz = line.split(',', 2)
        data.append(tuple(int(i) for i in xyz))
    return data

# Calculate the distance squared
def distance(vec1: Vec, vec2: Vec) -> int:
    x, y, z = vec1
    a, b, c = vec2
    return (x - a) ** 2 + (y - b) ** 2 + (z - c) ** 2

# Get sorted list of distances from i to j where i < j
def get_distances(data: List[Vec]) -> List[Tuple[int, int, int]]:
    distances: List[Tuple[int, int, int]] = sum(
        [[(i, i + 1 + j, distance(v1, v2)) for j, v2 in enumerate(data[i + 1:])] for i, v1 in enumerate(data[:-1])],
        start=[]    
    )
    return sorted(distances, key=lambda dist: dist[2])

def solve_part_1(data, sorted_distances):
    N = len(data)
    circuits: List[int] = [i for i in range(N)]
    for i, j, _ in sorted_distances[:1000]:
        circuit_i = circuits[i]
        circuit_j = circuits[j]
        if circuit_i != circuit_j:
            c = min(circuit_i, circuit_j)
            for k, circuit_k in enumerate(circuits):
                if circuit_k == circuit_i or circuit_k == circuit_j:
                    circuits[k] = c
    circuit_sizes = [circuits.count(c) for c in range(N)]
    return reduce(mul, sorted(circuit_sizes, reverse=True)[:3], 1)

def solve_part_2(data, sorted_distances):
    N = len(data)
    circuits: List[int] = [i for i in range(N)]
    for i, j, _ in sorted_distances:
        circuit_i = circuits[i]
        circuit_j = circuits[j]
        if circuit_i != circuit_j:
            c = min(circuit_i, circuit_j)
            for k, circuit_k in enumerate(circuits):
                if circuit_k == circuit_i or circuit_k == circuit_j:
                    circuits[k] = c
        if not any(circuits):
            # All boxes are part of circuit 0; all connected
            return data[i][0] * data[j][0]
    raise AssertionError('Not everything is connected. This should be impossible.')

if __name__ == "__main__":
    data = get_data()
    distances = get_distances(data)
    print(solve_part_1(data, distances))
    print(solve_part_2(data, distances))
