class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # duo-splitting algorithm. Time: O(n).
        # doubly binary search. essentially, we're splitting into parts with a left and right pointer just like regular binary search. but instead of deciding between a single pivot, we now decide between 2 ranges.
        # we know that if left number and pivot number are in ascending order, then the subarray MUST be in ascending order. and the right subarray must be the one where the rotation happens.
        # if our target is in the left subarray, simple binary search will do the trick!
        # if our target in in the right subarray, we should continue to use the duo-splitting algorithm
        # note that middle pivot will have only 1 subarray at max with rotated subarray.
        
        left, right = 0, len(nums) - 1 # define pointers

        while left <= right:
            
            middle = (right + left) // 2 # get middle index
            
            # check if any of the pointers match to target. only need to do for middle, but this is just sanity check for now...
            if nums[middle] == target:
                return middle
            
            if nums[left] <= nums[middle]: #sorted left section
                if nums[left] <= target <= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
                    
            else: # sorted right section
                if nums[middle] <= target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
        return -1
                    