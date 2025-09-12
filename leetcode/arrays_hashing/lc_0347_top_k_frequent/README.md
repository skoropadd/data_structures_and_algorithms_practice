---

# 347. Top K Frequent Elements

---

## Approach 1 — Hash Map + Min-Heap (Optimal when k ≪ n)

### Intuition

Count how often each number appears, then keep only the **k most frequent** in a **min-heap** by frequency.
If the heap grows beyond `k`, drop the smallest. This avoids sorting everything.

### Approach

1. Build a frequency map `num → count`.
2. Push `(count, num)` into a min-heap.
3. If heap size exceeds `k`, pop (removes the least frequent).
4. Extract the `k` numbers from the heap.

### Complexity

* Time: **O(n + u log k)** (u = #unique elements; building counts is O(n))
* Space: **O(u + k)**

### Code

```python3 []
from typing import List, Tuple
from collections import Counter
import heapq

def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    heap: List[Tuple[int, int]] = []
    for num, cnt in freq.items():
        heapq.heappush(heap, (cnt, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [heapq.heappop(heap)[1] for _ in range(len(heap))]
```

---

## Approach 2 — Hash Map + `heapq.nlargest` (Pythonic & concise)

### Intuition

Same idea as Approach 1, but use `heapq.nlargest` to directly select the top-k by frequency.

### Approach

1. Build `Counter(nums)`.
2. Call `heapq.nlargest(k, freq.items(), key=lambda x: x[1])`.
3. Return the numbers.

### Complexity

* Time: **O(n + u log k)**
* Space: **O(u)**

### Code

```python3 []
from typing import List, Tuple
from collections import Counter
import heapq

def top_k_frequent_nlargest(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    top: List[Tuple[int, int]] = heapq.nlargest(k, freq.items(), key=lambda x: x[1])
    return [num for num, _ in top]
```

---

## Approach 3 — Bucket Sort by Frequency (Linear time)

### Intuition

A number can’t appear more than `n` times.
Make `n+1` buckets where `bucket[i]` holds numbers with frequency `i`.
Then scan from high frequency down until you collect `k`.

### Approach

1. Build frequency map.
2. Create `buckets = [[] for _ in range(n+1)]`.
3. For each `(num, cnt)`, append `num` to `buckets[cnt]`.
4. Traverse buckets from `n → 1`, collect numbers until size `k`.

### Complexity

* Time: **O(n)** (build counts + bucket fill + single pass)
* Space: **O(n)**

### Code

```python3 []
from typing import List
from collections import Counter

def top_k_frequent_bucket(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for num, cnt in freq.items():
        buckets[cnt].append(num)
    res: List[int] = []
    for f in range(len(buckets) - 1, 0, -1):
        for num in buckets[f]:
            res.append(num)
            if len(res) == k:
                return res
    return res
```

---

## Approach 4 — Sort by Frequency (Simple but slower)

### Intuition

Count, then **sort** unique numbers by frequency descending and take top-k.

### Complexity

* Time: **O(n + u log u)** (due to sorting)
* Space: **O(u)**

### Code

```python3 []
from typing import List
from collections import Counter

def top_k_frequent_sort(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    return [num for num, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]
```

---

## Edge Cases & Notes

* If `k == len(set(nums))`, all unique elements are returned (any order is fine).
* For very large `n` with small `k`, **heap** approaches are ideal.
* If you want pure linear behavior and can afford buckets of size `n`, go with **bucket sort**.
* Output order is unspecified in the problem—any order is accepted.

---