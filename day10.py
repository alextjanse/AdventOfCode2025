from typing import List, Tuple
from heapq import heappush, heappop
from pulp import LpProblem, LpVariable, LpMinimize, LpStatus, lpSum, value
from aoc import read_file

def get_data() -> List[Tuple[int, List[int], List[int]]]:
    data = []
    for line in read_file(10, False):
        parts = line.split()
        target = sum(1 << i for i, c in enumerate(parts[0][1:-1]) if c == '#')
        buttons = [[int(i) for i in button[1:-1].split(',')] for button in parts[1:-1]]
        joltages = [int(i) for i in parts[-1][1:-1].split(',')]
        data.append((target, buttons, joltages))
    return data

def solve_lights(buttons: List[List[int]], target: int) -> int:
    states = [(0, 0)]
    visited_states = set()
    while states:
        steps, state = heappop(states)
        if state == target:
            return steps
        if state in visited_states:
            continue
        visited_states.add(state)
        for button in buttons:
            new_state = state
            for b in button:
                new_state = new_state ^ (1 << b)
            heappush(states, (steps + 1, new_state))
    raise RuntimeError(target, buttons, 'has no solution')

def solve_part_1(data):
    total = 0
    for target, buttons, _ in data:
        total += solve_lights(buttons, target)
    return total

def solve_joltages(buttons: List[List[int]], joltages: List[int]) -> int:
    N = len(joltages)
    M = len(buttons)

    B = [[] for _ in range(N)]
    for i, button in enumerate(buttons):
        for b in button:
            B[b].append(i)

    vars = []
    for i in range(M):
        vars.append(LpVariable(f'b{i}', lowBound=0, cat='Integer'))
    
    prob = LpProblem('myProblem', LpMinimize)
    prob.objective = lpSum(vars)
    for eq, bound in zip(B, joltages):
        prob += lpSum(vars[i] for i in eq) == bound

    status = prob.solve()
    print(LpStatus[status])
    for var in vars:
        print(var, value(var))
    return int(sum(map(value, vars)))

def solve_part_2(data):
    total = 0
    for target, buttons, joltages in data:
        total += solve_joltages(buttons, joltages)
    return total

if __name__ == "__main__":
    data = get_data()
    print(solve_part_1(data))
    print(solve_part_2(data))
