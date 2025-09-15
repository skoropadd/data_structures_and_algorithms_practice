from collections import defaultdict


def group_anagrams_hashmap(strs: list[str]) -> list[list[str]]:
    """
    Group Anagrams using a 26-length frequency vector per word.
    Time: O(n * k), Space: O(n * k) where k is average word length.
    Assumes lowercase 'a'..'z'. For broader alphabets use Counter-based key.
    """
    groups: dict[tuple[int, ...], list[str]] = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for c in word:
            count[ord(c) - ord("a")] += 1
        groups[tuple(count)].append(word)
    return list(groups.values())
