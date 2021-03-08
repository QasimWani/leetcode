class Solution:
    def maxArea(self, height: List[int]) -> int:
        #2 pointer approach where you move the shorter line inward.
        #Time: O(n)
        #Space: O(1)
        
        left, right = 0, len(height) - 1
        
        area = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]: #move left inward, i.e. left += 1
                left += 1
            else: #move right inward, i.e right -= 1
                right -= 1
            #recalculate total area
            area = max(area, (right - left) * min(height[left], height[right]))
        return area