class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i,j,k = 0, 1, len(nums)-1
        res = []
        nums.sort()
        while i < j < k:
            #assuming nums is sorted, even if isn't we can sort in O(nlogn)
            while j < k:
                #print(nums[i], nums[j], nums[k])
                cursum = nums[i] + nums[j] + nums[k]
                if cursum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j<k and nums[j]==nums[j-1]:
                        j += 1
                    while j<k and nums[k]==nums[k+1]:
                        k -= 1
                    # might be multiple same number triplets
                j += (cursum < 0)
                k -= (cursum > 0)
            i += 1
            while i<len(nums) and nums[i]==nums[i-1]:
                i += 1
            j = i + 1
            k = len(nums)-1
        return res