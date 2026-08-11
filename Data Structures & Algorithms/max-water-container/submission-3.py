class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = self.getArea(left, right, heights)
        while left <= right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            maxArea = max(maxArea, self.getArea(left, right, heights))
        return maxArea
        
    def getArea(self, left, right, heights) -> int:
        return ((right - left) * min(heights[left], heights[right]))


        