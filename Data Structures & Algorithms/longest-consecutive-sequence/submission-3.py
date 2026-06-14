class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxcount = 0
        for num in s:
            if num-1 in s:
                continue
            count = 1
            while num+1 in s:
                count += 1
                num += 1
            maxcount = max(maxcount, count)
        return maxcount