# 0217. Contains Duplicate — Arrays & Hashing

Organized as a step-by-step evolution:

---

## Strategy 0 — Brute Force (Compare All Pairs)

### Intuition
Check every pair; if any two are equal, there’s a duplicate.

### Approach
Two nested loops: compare nums[i] with nums[j] for all j > i.

### Complexity
- Time: O(n^2)
- Space: O(1)

### Code
```python
def contains_duplicate_bruteforce(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False
````

---

## Strategy 1 — Sorting Layer (Neighbor Check)

### Intuition

After sorting, duplicates become adjacent.

### Approach

Sort a copy, scan once comparing arr\[i] to arr\[i-1].

### Complexity

* Time: O(n log n) (sort)
* Space: O(1)\~O(log n) extra (impl-dependent)

### Code

```python
def contains_duplicate_sortscan(nums):
    arr = list(nums)
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return True
    return False
```

---

## Strategy 2 — Hashing Layer (Set Length Compare)

### Intuition

If unique count < total count, duplicates exist.

### Approach

Build set(nums) and compare lengths.

### Complexity

* Time: O(n)
* Space: O(n)

### Code

```python
def contains_duplicate_setlen(nums):
    return len(set(nums)) != len(nums)
```

---

## Strategy 3 — Refinement (Hashing + Early Exit)

### Intuition

Stop as soon as a repeat appears.

### Approach

Maintain a set; if x already in set, return True; else add.

### Complexity

* Time: O(n) average (best case early stop)
* Space: O(n)

### Code

```python
def contains_duplicate_setearly(nums):
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False
```

---

### Bonus — Dict as Set (works, but less idiomatic)

A dict also uses hashing; storing dummy values is redundant vs a set.

```python
def contains_duplicate_dictearly(nums):
    seen = {}
    for x in nums:
        if x in seen:
            return True
        seen[x] = True
    return False
```


