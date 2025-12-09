'''Advent of Code module'''

from typing import List

def read_file(day: int, test=False) -> List[str]:
    return open(f'data/{"test" if test else "in"}{day}.txt', 'r').readlines()