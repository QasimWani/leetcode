# Time: O(log n)
# Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # this is a version of rotated search problem but instead of a target, we must find minumum.
        # the logic stays pretty much the same. 
        
        left, right = 0, len(nums) - 1
        # if left val less than right val, then array must be sorted
        if nums[left] <= nums[right]:
            return nums[left]
        
        while left <= right:
            middle = (left + right) // 2
            
            # if we're currently at peak, then next number must be the lowest number
            if nums[middle] > nums[middle + 1]:
                return nums[middle + 1]
            # if we're currently at the lowest point, then the previous number must have been the peak
            if nums[middle - 1] > nums[middle]:
                return nums[middle]
            
            if nums[0] > nums[middle]: # min exists in left section
                right = middle - 1
            else:
                left = middle + 1
        return -1
            