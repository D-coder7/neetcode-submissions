class Solution:
    def trap(self, height: List[int]) -> int:
        maxh = 0
        heightSum = 0
        lspace = rspace = 0
        for i, h in enumerate(height):
            heightSum += h
            if h <= maxh:
                continue

            lspace += (h-maxh)*i
            maxh = h
        
        maxh = 0
        for i, h in enumerate(height[::-1]):
            #print(i, h)
            if h <= maxh:
                continue
            
            rspace += (h-maxh)*(i)
            maxh = h
        
        return maxh*len(height) - heightSum - lspace - rspace