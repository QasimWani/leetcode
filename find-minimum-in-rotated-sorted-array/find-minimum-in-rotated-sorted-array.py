# Time: O(log n)
# Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # start with the first element. if the first element is smaller than the last element, then it must be sorted
        if nums[0] <= nums[-1]:
            return nums[0]
        
        # find first peak and that should be the answer
        for i in range(len(nums) - 1):
            curr, next = nums[i], nums[i + 1]
            if curr > next: # currently at peak, next value must be the smallest value
                return next
        return curr