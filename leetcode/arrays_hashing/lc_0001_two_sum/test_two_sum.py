import pytest

from leetcode.arrays_hashing.lc_0001_two_sum.bruteforce_solution import (
    two_sum_bruteforce,
)
from leetcode.arrays_hashing.lc_0001_two_sum.hashmap_solution import two_sum_hashmap
from leetcode.arrays_hashing.lc_0001_two_sum.sort_solution import two_sum_sort

CASES = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([-1, -2, -3, -4, -5], -8),
    ([0, 4, 3, 0], 0),
    ([1, 5, 1, 5], 10),
]


def _assert_valid(nums: list[int], target: int, res: list[int]) -> None:
    assert len(res) == 2, "must return two indices"
    i, j = res
    n = len(nums)
    assert 0 <= i < n and 0 <= j < n and i != j, "indices must be distinct and in range"
    assert nums[i] + nums[j] == target, "pair must sum to target"


@pytest.mark.parametrize("nums,target", CASES)
def test_hashmap(nums, target):
    _assert_valid(nums, target, two_sum_hashmap(nums, target))


@pytest.mark.parametrize("nums,target", CASES)
def test_sort(nums, target):
    _assert_valid(nums, target, two_sum_sort(nums, target))


@pytest.mark.parametrize("nums,target", CASES)
def test_bruteforce(nums, target):
    _assert_valid(nums, target, two_sum_bruteforce(nums, target))
