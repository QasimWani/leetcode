class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ### so the idea is that the pivot now the middle element of nums.
        ### using this idea, we can first check which side of the array must 
        ### the target belong to. and once that is done, we can implement the 
        ### regular binary search to find the target element, if it exists.
        
        ### Time: O(log(n)) ; Space : O(1), done in-place with constant auxillary space
        
        if(not nums):
            return - 1
        
        left, right = 0, len(nums) - 1
        
        while(left <= right):
            mid_idx = (left + right) // 2
            
            if(nums[mid_idx] == target):
                return mid_idx
            
            if(nums[left] <= nums[mid_idx]):
                if nums[left] <= target <= nums[mid_idx]:
                    right = mid_idx - 1
                else:
                    left = mid_idx + 1
            else:
                if nums[mid_idx] <= target <= nums[right]:
                    left = mid_idx + 1
                else:
                    right = mid_idx - 1
        
        return -1
