class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortnums = list(nums)
        sortnums.sort()
        print(sortnums)
        currl = maxl = 1
        for i in range(1, len(sortnums)):
            if sortnums[i-1]+1 == sortnums[i]:
                currl += 1
            elif sortnums[i-1] == sortnums[i]:
                pass
            else:
                currl = 1
            maxl = max(maxl, currl)
        return maxl
