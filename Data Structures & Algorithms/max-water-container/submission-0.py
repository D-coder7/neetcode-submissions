class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAr = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                maxAr = max(maxAr, (j-i)*min(heights[i], heights[j]))
        return maxAr