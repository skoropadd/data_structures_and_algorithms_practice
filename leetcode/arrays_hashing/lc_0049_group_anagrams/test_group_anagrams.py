import pytest

from leetcode.arrays_hashing.lc_0049_group_anagrams.hashmap_solution import (
    group_anagrams_hashmap,
)
from leetcode.arrays_hashing.lc_0049_group_anagrams.sort_solution import (
    group_anagrams_sort,
)

CASES = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        {
            frozenset(("eat", "tea", "ate")),
            frozenset(("tan", "nat")),
            frozenset(("bat",)),
        },
    ),
    ([""], {frozenset(("",))}),
    (["a"], {frozenset(("a",))}),
    (
        ["ab", "ba", "ab"],
        {
            frozenset(("ab", "ba", "ab")),
        },
    ),
    (
        ["abc", "bca", "cab", "zzz"],
        {
            frozenset(("abc", "bca", "cab")),
            frozenset(("zzz",)),
        },
    ),
]


def _normalize(groups: list[list[str]]) -> set[frozenset[str]]:
    # Convert list of lists to a set of frozensets for order-insensitive comparison
    return {frozenset(g) for g in groups}


@pytest.mark.parametrize("strs,expected_sets", CASES)
def test_hashmap(strs, expected_sets):
    got = _normalize(group_anagrams_hashmap(strs))
    assert got == expected_sets


@pytest.mark.parametrize("strs,expected_sets", CASES)
def test_sort(strs, expected_sets):
    got = _normalize(group_anagrams_sort(strs))
    assert got == expected_sets
