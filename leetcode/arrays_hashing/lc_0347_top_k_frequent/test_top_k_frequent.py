import pytest

from leetcode.arrays_hashing.lc_0347_top_k_frequent.bucket_solution import (
    top_k_frequent_bucket,
)
from leetcode.arrays_hashing.lc_0347_top_k_frequent.heap_solution import (
    top_k_frequent_heap,
)
from leetcode.arrays_hashing.lc_0347_top_k_frequent.nlargest_solution import (
    top_k_frequent_nlargest,
)
from leetcode.arrays_hashing.lc_0347_top_k_frequent.sort_solution import (
    top_k_frequent_sort,
)

CASES = [
    ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
    ([1], 1, {1}),
    ([4, 1, -1, 2, -1, 2, 3], 2, {-1, 2}),
    ([5, 5, 5, 5, 6, 6, 7], 1, {5}),
    # all freq=1 -> any 3 are valid
    ([1, 2, 3, 4, 5, 6], 3, None),
]


@pytest.mark.parametrize("nums,k,expected_set", CASES)
def test_heap(nums, k, expected_set):
    res = top_k_frequent_heap(nums, k)
    if expected_set is None:
        assert len(res) == k
        assert set(res).issubset(set(nums))
    else:
        assert set(res) == expected_set


@pytest.mark.parametrize("nums,k,expected_set", CASES)
def test_nlargest(nums, k, expected_set):
    res = top_k_frequent_nlargest(nums, k)
    if expected_set is None:
        assert len(res) == k
        assert set(res).issubset(set(nums))
    else:
        assert set(res) == expected_set


@pytest.mark.parametrize("nums,k,expected_set", CASES)
def test_bucket(nums, k, expected_set):
    res = top_k_frequent_bucket(nums, k)
    if expected_set is None:
        assert len(res) == k
        assert set(res).issubset(set(nums))
    else:
        assert set(res) == expected_set


@pytest.mark.parametrize("nums,k,expected_set", CASES)
def test_sort(nums, k, expected_set):
    res = top_k_frequent_sort(nums, k)
    if expected_set is None:
        assert len(res) == k
        assert set(res).issubset(set(nums))
    else:
        assert set(res) == expected_set
