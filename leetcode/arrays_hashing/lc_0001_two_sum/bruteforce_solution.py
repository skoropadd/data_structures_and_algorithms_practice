def two_sum_bruteforce(nums: list[int], target: int) -> list[int]:
    """Check all pairs; O(n^2) time, O(1) space."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
