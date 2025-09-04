def contains_duplicate_setlen(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)
