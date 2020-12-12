from datetime import datetime
from typing import (
    List,
)
import re


def read_bags(path: str) -> List[List[str]]:
    """Read groups from input file, skip last trailing newline and split to list of lists."""
    with open(path, 'r') as f:
        lines = f.read()[:-1].splitlines()
        p = re.compile('\\w+[a-zA-Z0-9 ]\\w+(?=\\sbag)')
        return (
            [p.findall(line) for line in lines],
            lines,
            [line for line in lines if line.startswith('shiny gold bag')]
        )


def can_hold_shiny_golds(bags, color: str = 'shiny gold', can_hold=[]):
    for bag in bags:
        if color in bag[1:]:
            can_hold.append(bag[0])
            can_hold_shiny_golds(bags, color=bag[0], can_hold=can_hold)
    return len(set(can_hold))


def traverse_count(bags, lines, parent='shiny gold', cap=0):
    """This is terrible, but it works..."""
    for bag in bags:
        if bag[0] == parent:
            for b in bag[1:]:
                desc = ''
                for line in lines:
                    if line.startswith(parent):
                        desc = line
                        break
                if 'no other bags' not in desc:
                    amt = int(desc.split(b)[0].strip()[-1])
                else:
                    amt = 0
                subbags = traverse_count(bags, lines, parent=b, cap=0)
                cap += amt + subbags*amt
    return cap


if __name__ == '__main__':
    bags, lines, premise = read_bags('input.txt')
    start = datetime.now()
    part_1 = can_hold_shiny_golds(bags)
    end = datetime.now()
    print(f'Part 1: found \'{part_1}\' bags of different colors that can hold shiny gold bags, '
          f'execution time {(end-start).total_seconds()*1000}ms')
    start = datetime.now()
    part_2 = traverse_count(bags, lines)
    end = datetime.now()
    print(f'Part 2: the ultimate depth of a shiny gold bag is \'{part_2}\' '
          f'execution time {(end-start).total_seconds()*1000}ms')
