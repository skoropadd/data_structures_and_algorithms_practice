def is_anagram_hashmap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS: dict[str, int] = {}
    countT: dict[str, int] = {}
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    return countS == countT
