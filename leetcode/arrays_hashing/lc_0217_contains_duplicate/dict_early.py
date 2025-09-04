def contains_duplicate_dictearly(nums: list[int]) -> bool:
    seen = {}
    for x in nums:
        if x in seen:
            return True
        seen[x] = True  # dummy value
    return False
