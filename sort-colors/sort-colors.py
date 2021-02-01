class Solution:
    def sortColors(self, nums: List[int], low=None, high=None) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Sorting using Quicksort
        #Time: O(nlogn)
        #Space: O(1), in-place
        if(low == None):
            low, high = 0, len(nums) - 1
            
        if(low < high):
            pivot = self.helper(nums, low, high) #get pivot index. 
            #perform recursion on left & right paritions
            self.sortColors(nums, low, pivot - 1)
            self.sortColors(nums, pivot + 1, high)
            
            
    def helper(self, nums, low, high):
        i = low - 1
        pivot = nums[high]
        
        #Goal: all elements to the left of pivot < pivot. All elements to right of pivot > pivot.
        #Let i be the index for leftPivot, i.e. checks to see if current element < pivot.
        #Let j be the index for rightPivot, i.e. checks to see if current element > pivot.
        for j in range(low, high):
            if(nums[j] <= pivot):
                #swap i and j
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        
        i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i