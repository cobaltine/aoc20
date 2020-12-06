from typing import (
    List,
    Tuple,
)
from datetime import datetime


def count_answers(group_answers: str) -> Tuple[int, int]:
    group_unique_answers = 0
    group_same_answers = 0
    for g in group_answers:
        unique_answers = []
        for answers in g:
            unique_answers.extend(a for a in answers if a not in unique_answers)
        group_unique_answers += len(unique_answers)

        for a in unique_answers:
            all_yes = True
            for answers in g:
                if a not in answers:
                    all_yes = False
                    break
            if all_yes:
                group_same_answers += 1
    return (group_unique_answers, group_same_answers)


def read_group_answers(path: str) -> List[List[str]]:
    """Read groups from input file, skip last trailing newline and split to list of lists."""
    with open(path, 'r') as f:
        return [g.split('\n') for g in f.read()[:-1].split('\n\n')]


if __name__ == '__main__':
    start = datetime.now()
    group_answers = read_group_answers(path='input.txt')
    group_unique_answers, group_same_answers = count_answers(group_answers)
    end = datetime.now()
    print(f'Part 1: groups had a total of {group_unique_answers} unique answers')
    print((f'Part 2: groups had a total of {group_same_answers} same answers '
           '(entire group answered \'yes\' to the same question)'))
    print(f'Execution completed in {(end-start).total_seconds()*1000}ms')
