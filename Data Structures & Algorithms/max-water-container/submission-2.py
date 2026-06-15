class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        lmax = [0]*len(heights)
        rmax = [0]*len(heights)
        # these lists don't actually store the max vol, only the max vol with curr pillar as shorter pillar
        while l < r:
            if heights[l] > heights[r]:
                lmax[r] = (r-l)*heights[r]
                r -= 1
            elif heights[l] < heights[r]:
                rmax[l] = (r-l)*heights[l]
                l += 1
            else:
                lmax[r] = (r-l)*heights[l]
                rmax[l] = (r-l)*heights[r]
                l += 1
                r -= 1
            # not storing the lmax vals of l pointer and rmax vals of r pointer
            # for rmax of l pointer, r pointer should start from end but not needed as
            # r-index for true rmax of l would already have greater lmax
        return max(max(lmax), max(rmax))