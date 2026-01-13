from collections import defaultdict
from typing import Dict, List, Set
from aoc import read_file

def get_data() -> Dict[str, Set[str]]:
    data = dict()
    for line in read_file(11):
        parts = line.split()
        header = parts[0][:-1]
        data[header] = set(parts[1:])
    return data

def sort_topologically(graph: Dict[str, Set[str]]) -> List[str]:
    L = []

    unvisited = set(graph.keys())
    visited = set()
    visiting = set()
    
    def visit(node: str) -> None:
        if node in visited:
            return
        if node in visiting:
            raise ValueError(node, 'is part of a cycle')
        unvisited.discard(node)
        visiting.add(node)
        for nb in graph.get(node, []):
            visit(nb)
        visiting.remove(node)
        visited.add(node)
        L.append(node)

    while unvisited:
        node = unvisited.pop()
        visit(node)
    return L[::-1]

def get_path_count(graph: Dict[str, Set[str]], topo: List[str], start: str, end: str) -> int:
    path_count: Dict[str, int] = defaultdict(lambda: 0)
    start_index = topo.index(start)
    end_index = topo.index(end)
    path_count[start] = 1
    for node in topo[start_index:end_index]:
        p = path_count[node]
        for nb in graph.get(node, []):
            path_count[nb] += p
    return path_count[end]

def solve_part_1(graph: Dict[str, Set[str]], topo: List[str]) -> int:
    return get_path_count(graph, topo, 'you', 'out')

def solve_part_2(graph: Dict[str, Set[str]], topo: List[str]) -> int:
    dac_index = topo.index('dac')
    fft_index = topo.index('fft')
    if dac_index < fft_index:
        return (get_path_count(graph, topo, 'svr', 'dac') *
                get_path_count(graph, topo, 'dac', 'fft') *
                get_path_count(graph, topo, 'fft', 'out')
                )
    else:
        return (get_path_count(graph, topo, 'svr', 'fft') *
                get_path_count(graph, topo, 'fft', 'dac') *
                get_path_count(graph, topo, 'dac', 'out')
                )

if __name__ == "__main__":
    data = get_data()
    topo = sort_topologically(data)
    print(solve_part_1(data, topo))
    print(solve_part_2(data, topo))
