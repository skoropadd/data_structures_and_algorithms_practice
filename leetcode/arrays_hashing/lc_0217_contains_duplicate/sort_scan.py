def contains_duplicate_sortscan(nums: list[int]) -> bool:
    arr = list(nums)  # avoid mutating caller
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            return True
    return False
