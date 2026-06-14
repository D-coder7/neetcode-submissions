class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0: break
            j = i + 1
            k = len(nums) - 1

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
        return res