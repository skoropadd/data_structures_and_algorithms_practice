def two_sum_hashmap(nums: list[int], target: int) -> list[int]:
    """One-pass hash map: O(n) time, O(n) space."""
    indices: dict[int, int] = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in indices:
            return [indices[diff], i]
        indices[num] = i
    # If problem guarantees an answer exists, we won't reach here.
    return []
