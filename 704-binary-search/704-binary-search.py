class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #TEMP
	    # return self.helper(nums, target, 0, len(nums) - 1)
        return self.iterative_sol(nums, target)

    def helper(self, array, target, left, right):
        if(left > right):
            return -1
        middle = (left + right)//2
        potential_match = array[middle]

        if(target == potential_match):
            return middle
        if(target > potential_match):
            return self.helper(array, target, middle + 1, right)
        else:
            return self.helper(array, target, left, middle - 1)
    
    def iterative_sol(self, array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            middle = (left + right) // 2
            if array[middle] == target:
                return middle
            if target < array[middle]: # target is on the left side
                right = middle - 1
            else: # target is on the right side
                left = middle + 1
        return -1
                