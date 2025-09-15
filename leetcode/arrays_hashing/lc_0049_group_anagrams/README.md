---

# Intuition

Anagrams share the same multiset of characters. If we **count characters** for each word, anagrams will have identical count vectors.

# Approach

* Create a hash map from a **26-length character count tuple** to a list of words.
* For each word, build `count[0..25]` where index = `ord(c) - ord('a')`.
* Use the tuple of counts as the key and append the word to its group.
* Return the grouped lists.

# Complexity

* Time complexity: $O(n \cdot k)$ where $n$ is the number of words and $k$ is the average word length (we scan each character once).
* Space complexity: $O(n \cdot k)$ to store the grouped words (the key tuples are $O(1)$ each since size 26 is constant).

# Code

```python3 []
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0] * 26  # for 'a'..'z'
            for c in word:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)  # immutable → usable as dict key
            groups[key].append(word)
        return list(groups.values())
```

---

# Intuition

Anagrams become identical after **sorting** their characters. The sorted string can serve as a canonical key.

# Approach

* For each word, compute `key = "".join(sorted(word))`.
* Use this sorted string as the key in a hash map to collect words in the same group.
* Return all grouped lists.

# Complexity

* Time complexity: $O(n \cdot k \log k)$ — sorting each word of length $k$.
* Space complexity: $O(n \cdot k)$ to store the grouped words and keys.

# Code

```python3 []
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            res[key].append(word)
        return list(res.values())
```

> Note: Both versions assume lowercase English letters. If inputs can include uppercase or Unicode, the logic still works; for the counting approach you’d switch to a `Counter` or a larger mapping instead of a fixed size-26 array.
