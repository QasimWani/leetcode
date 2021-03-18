class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #basically find the first instance of negative -> positive shift. and use 2 pointers left and right and compare which element is smaller
        #and store the squares of the numbers based on 2 pointer comparison. After this, move both left and right pointer outwards. Note that left
        #and right pointers may be unbalanced so as soon as one hits the end, we can just take the remaining elements from the other pointer and store
        #the squares accordingly.
        
        #Time: O(n)
        #Space: O(n)
        
        #first check if negative elements exist. if they don't simply square and voila.
        if nums[0] >= 0:
            return [x**2 for x in nums]
        #if all elements are negative, return the reverse square
        if nums[-1] < 0:
            return [x**2 for x in reversed(nums)]
        
        #now, there is a guarantee of a mix of negative and positive numbers
        #find index of first positive number
        for i, x in enumerate(nums):
            if x >= 0:
                left, right = i - 1, i
                break

        arr = []
        #compare left and right pointer values. if squared (nums[left] < nums[right]) add all right pointer values while that condition is true.
        #once it's false, do the opposite, i.e. move the left pointer outwards until right number < left number. continue this process until both hit an edge.
        while right - left <= len(nums):
            mod_left = float('inf')
            mod_right = float('inf')
            if left >= 0:
                mod_left = nums[left]**2
                
            if right < len(nums):
                mod_right = nums[right]**2
            
            if mod_left <= mod_right and mod_left < float('inf'):
                arr.append(mod_left)
                left -= 1
            elif(mod_left > mod_right and mod_right < float('inf')):
                arr.append(mod_right)
                right += 1
            
        return arr