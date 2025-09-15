def two_sum_sort(nums: list[int], target: int) -> list[int]:
    """Sort by value but keep original indices; two-pointer scan."""
    arr = [(num, i) for i, num in enumerate(nums)]
    arr.sort(key=lambda x: x[0])

    i, j = 0, len(arr) - 1
    while i < j:
        s = arr[i][0] + arr[j][0]
        if s == target:
            return [arr[i][1], arr[j][1]]
        if s < target:
            i += 1
        else:
            j -= 1
    return []
