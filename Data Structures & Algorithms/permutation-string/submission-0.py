class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1) #window length
        s1Count = Counter(s1)
        s2Count = Counter(s2[:k-1])

        for i in range(k-1, len(s2)):
            s2Count[s2[i]] = 1 + s2Count.get(s2[i], 0)
            #print(s2Count)
            if s2Count == s1Count:
                return True
            s2Count[s2[i-k+1]] -= 1
            if s2Count[s2[i-k+1]] == 0:
                del s2Count[s2[i-k+1]]
        return False