from collections import Counter


def top_k_frequent_sort(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    items_sorted = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [num for num, _ in items_sorted[:k]]
