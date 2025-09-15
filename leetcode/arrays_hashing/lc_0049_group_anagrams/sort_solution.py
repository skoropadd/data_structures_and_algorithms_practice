from collections import defaultdict


def group_anagrams_sort(strs: list[str]) -> list[list[str]]:
    """
    Group Anagrams by sorting each word as a canonical key.
    Time: O(n * k log k), Space: O(n * k).
    Works for any characters that can be compared/sorted.
    """
    groups: dict[str, list[str]] = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
