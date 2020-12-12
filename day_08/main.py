from datetime import datetime
from typing import (
    List,
    Tuple,
)
Instruction = Tuple[str, int]


def read_instructions(path: str) -> List[List[str]]:
    with open(path, 'r') as f:
        return [[lin[:3], int(lin[4:])] for lin in f.read()[:-1].splitlines()]


def switch_op(op):
    if op == 'jmp':
        return 'nop'
    return 'jmp'


def execute(inst: List[Instruction], pos: int = 0, val: int = 0, switch_pos: int = -1):
    executed = []
    terminated = False
    while True:
        # Termination logic
        if executed.count(pos) > 1:
            terminated = True
            break
        elif pos >= len(inst):
            break

        # Operation switch invocation
        op = switch_op(inst[pos][0]) if switch_pos == pos else inst[pos][0]

        # Position and value manipulation
        if op == 'acc':
            val += inst[pos][1]

        if op == 'jmp':
            pos += inst[pos][1]
        else:
            pos += 1

        executed.append(pos)

    return val, terminated


def permutate(inst: List[Instruction]) -> Tuple[int, int]:
    pos = 0
    for i in range(len(inst)):
        if inst[i][0] != 'acc':
            val, terminated = execute(inst, switch_pos=i)
            if not terminated:
                return val, pos
    return -1, -1


if __name__ == '__main__':
    inst = read_instructions('input.txt')
    start = datetime.now()
    val_1, _ = execute(inst)
    end = datetime.now()
    print(f'Part 1: before termination, accumulator was at value \'{val_1}\', '
          f'completed in {(end-start).total_seconds()*1000}ms')
    val_2, pos = permutate(inst)
    print(f'Part 2: before termination, accumulator was at value \'{val_2}\', '
          f'completed in {(end-start).total_seconds()*1000}ms')
    end = datetime.now()
