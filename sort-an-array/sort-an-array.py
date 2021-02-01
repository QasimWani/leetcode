class Solution:
    def sortArray(self, nums: List[int], low=None, high=None) -> List[int]:
        #using quicksort
        #Time: O(nlogn)
        #Space: O(1)
        if(low is None):
            low = 0; high = len(nums) - 1
        
        if(low < high):
            parition = self.helper(nums, low, high)
            #partiion and perform recursion
            self.sortArray(nums, low, parition - 1)
            self.sortArray(nums, parition, high)
        
        return nums
    
    def helper(self, nums, low, high):
        i = low - 1
        pivot = nums[high]
        
        for j in range(low, high):
            if(nums[j] <= pivot):#swap
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[high] = nums[high], nums[i]
        return i
        