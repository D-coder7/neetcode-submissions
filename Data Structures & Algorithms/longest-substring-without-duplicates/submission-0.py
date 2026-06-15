class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        strset = set()
        l,r = 0,0
        maxlen = 0

        while r < len(s):
            while s[r] in strset:
                strset.remove(s[l])
                l += 1
            strset.add(s[r])
            maxlen = max(maxlen, r-l+1)
            r += 1
        
        return maxlen