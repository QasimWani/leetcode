class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_ = nums[0]
        if len(nums) < 2:
            return min_
        
        for i in range(len(nums) - 1):
            curr, next = nums[i], nums[i + 1]
            if curr > next:
                return next
        return min(min_, curr)