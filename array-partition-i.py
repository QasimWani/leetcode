#Time: O(nlogn)
#Space: O(1)
​
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        n = len(nums)//2
        if(n == 1):
            return min(nums)
        
        nums.sort(reverse=True) #in-order sorting.
        
        #perform n slices and find the max.
        i = 1
        sum = 0
        while(i < len(nums)):
            sum += nums[i]
            i += 2
            
        return sum
