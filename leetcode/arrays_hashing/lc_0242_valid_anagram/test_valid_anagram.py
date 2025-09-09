import pytest

from leetcode.arrays_hashing.lc_0242_valid_anagram.hashmap_solution import (
    is_anagram_hashmap,
)
from leetcode.arrays_hashing.lc_0242_valid_anagram.sort_solution import is_anagram_sort

CASES = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("", "", True),
    ("a", "a", True),
    ("ab", "ba", True),
    ("aacc", "ccac", False),
]


@pytest.mark.parametrize("s, t, expected", CASES)
def test_valid_anagram(s, t, expected):
    assert is_anagram_sort(s, t) == expected
    assert is_anagram_hashmap(s, t) == expected
