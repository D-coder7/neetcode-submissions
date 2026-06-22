class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charMap = Counter(t)
        minStr = t + s + 'a'
        matches = 0
        
        l = 0
        for r,c in enumerate(s):
            #print(minStr)
            if c in charMap:
                charMap[c] -= 1
                #print(charMap)
                if charMap[c] == 0:
                    matches += 1
            
                    while matches == len(charMap): 
                        if len(minStr) > r-l+1:
                            minStr = s[l:r+1]
                        
                        if s[l] in charMap:
                            charMap[s[l]] += 1
                            if charMap[s[l]] > 0:
                                matches -= 1
                        l += 1

        return minStr if len(minStr) <= len(s) else ""