import heapq
from collections import Counter


def top_k_frequent_nlargest(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    top: list[tuple[int, int]] = heapq.nlargest(k, freq.items(), key=lambda x: x[1])
    return [num for num, _ in top]
