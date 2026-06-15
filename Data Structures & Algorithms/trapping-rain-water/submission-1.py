class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = rmax = 0
        l,r = 0, len(height)-1
        vol = 0

        while l < r:
            #print(height[l], height[r])
            if height[l] < height[r]:
                lmax = max(lmax, height[l])
                vol += lmax - height[l]
                l += 1
            else:
                rmax = max(rmax, height[r])
                vol += rmax - height[r]
                r -= 1
        return vol
                