class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #two pass algorithm. first pass - find out how many zeros exist and append
        #those many elements to the array.
        #second pass - remove the elements for all zero positions in the original array
        
        #Time: O(n)
        #Space: O(1)
        
        num_zeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                num_zeros += 1
                nums.append(0)
        rem = 0
        for i in range(len(nums) - num_zeros):
            if nums[i - rem] == 0:
                nums.pop(i - rem)
                rem += 1