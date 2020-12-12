from datetime import datetime
from typing import (
    List,
    Tuple,
)
Instruction = Tuple[str, int]


def read_nums(path: str) -> List[List[str]]:
    with open(path, 'r') as f:
        return [int(num) for num in f.read()[:-1].splitlines()]


def find_pair_sum(nums: List[int], target: int) -> bool:
    for num in nums:
        for num2 in nums:
            if num+num2 == target:
                return True
    return False


def find_hax(nums: List[int], outlier: int) -> Tuple[int, int]:
    for i in range(len(nums)):
        bump = 1
        sum = nums[i]
        while (i+bump) < len(nums):
            sum += nums[i+bump]
            if sum == outlier:
                return min(nums[i:i+bump]), max(nums[i:i+bump])
            elif sum > outlier:
                break
            bump += 1
    return -1, -1


def find_outlier(nums: List[int], preamble: int) -> int:
    for i in range(len(nums)):
        found = find_pair_sum(nums[i-preamble:i], nums[i])
        if not found and i > preamble:
            return nums[i]
    return -1


if __name__ == '__main__':
    nums = read_nums('input.txt')
    start = datetime.now()
    outlier = find_outlier(nums, 25)
    end = datetime.now()
    print(f'Part 1: found outlier value \'{outlier}\', '
          f'execution time {(end-start).total_seconds()*1000}ms')
    min, max = find_hax(nums, outlier)
    end = datetime.now()
    print(f'Part 2: found min \'{min}\' and max \'{max}\' with a sum of {min+max}, '
          f'execution time {(end-start).total_seconds()*1000}ms')
