class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charMap = Counter(t)
        minStr = t + s
        matches = 0
        
        l = 0
        for r,c in enumerate(s):
            #print(minStr)
            if c in charMap:
                charMap[c] -= 1
                #print(charMap)
                if charMap[c] == 0:
                    matches += 1
            
                    if matches == len(charMap): 
                        while l<r and (s[l] not in charMap or charMap.get(s[l], -1) != 0):
                            if s[l] in charMap:
                                charMap[s[l]] += 1
                            l += 1

                        if len(minStr) > r-l+1:
                            minStr = s[l:r+1]
                        
                        charMap[s[l]] += 1
                        l += 1
                        matches -= 1

        return minStr if len(minStr) <= len(s) else ""