from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] += 1
        for c in t:
            hashmap[c] -= 1
        for  k in hashmap:
            if hashmap[k] != 0:
                return False
        return True