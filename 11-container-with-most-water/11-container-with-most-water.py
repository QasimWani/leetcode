class Solution:
    def maxArea(self, height: List[int]) -> int:
        #area maximization. i.e. max_width x max_height.
        #leftmost and rightmost pointer.
        #in that case, the height is 1 and width is 8. area = 8
        #now, say we move left pointer by 1 to the right and leave right pointer as is. Now, the area will be 7 x 7 = 49.
        #the algorithm essentially says to move the pointer with smallest height of the two. because we start with maximum width possible, the only other way to maximize area is by maximizing height, hence 
        #iterator solely based on height of the two pillars. 
        # terminating condition is if they overlap, ofc.
        
        left, right = 0, len(height) - 1
        max_area = float('-inf')
        
        while left <= right:
            h = min(height[left], height[right])
            area = (right - left) * h
            max_area = max(max_area, area)
            if height[left] == h: # min height is left, traverse left by 1.
                left += 1
            else:
                right -= 1
        return max_area
            
            
        
        
            