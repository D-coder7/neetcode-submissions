class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        countzer =0
        for n in nums:
            if n:
                prod *= n
            else:
                countzer += 1
        if countzer > 1:
            ans = [0 for n in nums]
        elif countzer == 1:
            ans = [0 if n else prod for n in nums]
        else:
            ans = [prod//n for n in nums]
        return ans