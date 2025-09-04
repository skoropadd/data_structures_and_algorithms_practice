import pytest

from leetcode.arrays_hashing.lc_0217_contains_duplicate.brute_force import (
    contains_duplicate_bruteforce,
)
from leetcode.arrays_hashing.lc_0217_contains_duplicate.dict_early import (
    contains_duplicate_dictearly,
)
from leetcode.arrays_hashing.lc_0217_contains_duplicate.set_early import (
    contains_duplicate_setearly,
)
from leetcode.arrays_hashing.lc_0217_contains_duplicate.set_len import (
    contains_duplicate_setlen,
)
from leetcode.arrays_hashing.lc_0217_contains_duplicate.sort_scan import (
    contains_duplicate_sortscan,
)

CASES = [
    ([], False),
    ([0], False),
    ([1, 2, 3, 4], False),
    ([1, 2, 3, 1], True),
    ([-1, -1], True),
    ([10] * 1000, True),
    (list(range(10000)), False),
]


@pytest.mark.parametrize("arr, expected", CASES)
def test_all_strategies(arr, expected):
    assert contains_duplicate_bruteforce(arr) == expected
    assert contains_duplicate_sortscan(arr) == expected
    assert contains_duplicate_setlen(arr) == expected
    assert contains_duplicate_setearly(arr) == expected
    assert contains_duplicate_dictearly(arr) == expected
