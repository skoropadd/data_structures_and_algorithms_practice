### Approach 1: Sorting

#### Intuition
If two strings are anagrams, then sorting their characters will produce identical sequences.

#### Approach
1. If the lengths of the strings differ, return `False`.  
2. Sort both strings.  
3. Compare the sorted results — if they match, return `True`.  

#### Complexity
- **Time complexity:** O(n log n), sorting dominates.  
- **Space complexity:** O(1) if sorting in place, O(n) if new arrays are created.  

#### Code
```python3 []
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        return sorted(s) == sorted(t)
````

---

### Approach 2: Hash Map (Frequency Counter)

#### Intuition

Instead of sorting, we can count the frequency of each character in both strings.
If the frequency distributions are identical, the strings are anagrams.

#### Approach

1. If the lengths differ, return `False`.
2. Use two hash maps (`dict`) to count characters in each string.
3. Compare the two hash maps; if equal, return `True`.

#### Complexity

* **Time complexity:** O(n), where n is the length of the strings.
* **Space complexity:** O(1) if the alphabet is fixed (like lowercase English letters).

#### Code

```python3 []
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
```