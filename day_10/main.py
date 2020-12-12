from datetime import datetime
from typing import (
    Dict,
    List,
)


def read_adapters(path: str) -> List[List[str]]:
    with open(path, 'r') as f:
        adapters = [int(num) for num in f.read()[:-1].splitlines()]
        adapters.sort()
        adapters.append(max(adapters)+3)
        return adapters


def find_adapters(adapters: List[int]) -> Dict:
    res = {}
    prev = 0
    for i in range(len(adapters)):
        for r in range(1, 4):
            if adapters[i] - 3 <= adapters[i]-r <= prev:
                prev = adapters[i]
                if r not in res.keys():
                    res[r] = [adapters[i]]
                else:
                    res[r].append(adapters[i])
                break
    return res


def options(adapters: List[int], i: int, hits: List[int]) -> Dict:
    for i in range(1, len(adapters)):
        hits[i] = hits[i-1]
        if i > 1 and adapters[i]-adapters[i-2] <= 3:
            hits[i] += hits[i-2]
        if i > 2 and adapters[i]-adapters[i-3] <= 3:
            hits[i] += hits[i-3]
    return hits[i]


if __name__ == '__main__':
    adapters = read_adapters('input.txt')
    start = datetime.now()
    res = find_adapters(adapters)
    end = datetime.now()
    print(f'Part 1: found \'{len(res[1])+len(res[3])}\' adapters, with 1*3 adapter counts totalling {len(res[1])*len(res[3])}, '
          f'execution time {(end-start).total_seconds()*1000}ms')
    start = datetime.now()
    adapters.insert(0, 0)
    opts = options(adapters=adapters, i=0, hits=([1]*len(adapters)))
    end = datetime.now()
    print(f'Part 2: found \'{opts}\' different configurations, '
          f'execution time {(end-start).total_seconds()*1000}ms')
