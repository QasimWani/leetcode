class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #optimal solution. We swap all non-zero elements based on their positions.
        #Time: O(n)
        #Space: O(1)
        
        current_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[current_pos] = nums[current_pos], nums[i]
                current_pos += 1