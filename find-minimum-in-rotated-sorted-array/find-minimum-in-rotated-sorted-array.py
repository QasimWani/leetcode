class Solution:
    def findMin(self, nums: List[int]) -> int:
        # start with the first element. if the first element is smaller than the last element, then it must be sorted
        if nums[0] <= nums[-1]:
            return nums[0]
        
        middle = len(nums) // 2
        
        if nums[-1] < nums[middle]: # smallest element on the right - middle side
            ans = nums[-1]
            i = len(nums) - 1
            while i >= middle:
                if ans >= nums[i]:
                    ans = nums[i]
                else:
                    return ans
                i -= 1
                
        else: # smallest element on the middle - left side
            ans = nums[middle]
            i = middle
            while i >= 0:
                if ans >= nums[i]:
                    ans = nums[i]
                else:
                    return ans
                
                i -= 1
        return None
                
                
            