class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixl = [1]*n
        suffixl = [1]*n
        for i in range(1, n):
            prefixl[i] = prefixl[i-1]*nums[i-1]
        for i in range(n-2, -1, -1):
            suffixl[i] = suffixl[i+1]*nums[i+1]
        print(prefixl)
        print(suffixl)
        return [prefixl[i]*suffixl[i] for i in range(n)]