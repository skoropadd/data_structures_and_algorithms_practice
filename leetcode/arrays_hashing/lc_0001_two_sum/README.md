---

## **Approach 1: Brute Force**

### Intuition

The simplest way is to check all possible pairs in the array and see if any sum to the target.

### Approach

1. Iterate over every index `i`.
2. For each `i`, iterate over every index `j > i`.
3. If `nums[i] + nums[j] == target`, return `[i, j]`.

### Complexity

* **Time complexity:** O(n²)
* **Space complexity:** O(1)

### Code

```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

## **Approach 2: Sorting + Two Pointers**

### Intuition

Sorting allows us to use the two-pointer technique to find two numbers whose sum is the target.
Since we need the original indices, we must pair each number with its index before sorting.

### Approach

1. Create an array of pairs `(num, index)`.
2. Sort this array by number.
3. Use two pointers: one at the start, one at the end.
4. Move pointers inward until their sum equals the target.
5. Return their original indices.

### Complexity

* **Time complexity:** O(n log n) (due to sorting)
* **Space complexity:** O(n) (to store number-index pairs)

### Code

```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort()

        i, j = 0, len(arr) - 1
        while i < j:
            curr = arr[i][0] + arr[j][0]
            if curr == target:
                return [arr[i][1], arr[j][1]]
            elif curr < target:
                i += 1
            else:
                j -= 1
```

---

## **Approach 3: Hash Map**

### Intuition

Instead of searching, we can store numbers in a hash map while iterating.
For each number, check if its complement (`target - num`) already exists in the map.

### Approach

1. Create an empty dictionary `indices`.
2. Iterate over the array with index `i` and value `num`.
3. Compute `diff = target - num`.
4. If `diff` exists in the dictionary, return `[indices[diff], i]`.
5. Otherwise, store `indices[num] = i`.

### Complexity

* **Time complexity:** O(n)
* **Space complexity:** O(n)

### Code

```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices:
                return [indices[diff], i]
            indices[num] = i
```

---