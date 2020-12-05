from typing import List
from datetime import datetime


def decode_seats(enc: List[str]) -> List[int]:
    """Decode alphabetical strings into numerical binary format strings and return as a sorted list."""
    decoded = []
    for line in enc:
        row = int(line[0:7].replace('F', '0').replace('B', '1'), base=2)
        col = int(line[7:].replace('L', '0').replace('R', '1'), base=2)
        decoded.append(row * 8 + col)
    decoded.sort()
    return decoded


def find_my_seat(seats: List[int]) -> int:
    """Find the seat which fails the increment check (my seat)."""
    for i in range(0, len(seats[1:])):
        if seats[0]+i not in seats:
            return seats[0]+i
    return -1


def read_input(path: str) -> List[str]:
    """Read input data from file, split into a list of strings."""
    with open(path, 'r') as f:
        return f.read().splitlines()


if __name__ == '__main__':
    start = datetime.now()
    input = read_input(path='input.txt')
    decoded = decode_seats(enc=input)
    print(f'Part 1: the highest seat ID on the list is \'{decoded[-1]}\'')
    print(f'Part 2: the seat ID missing (my seat!) is: \'{find_my_seat(decoded)}\'')
    end = datetime.now()
    print(f'Execution completed in {(end-start).total_seconds()*1000}ms')
