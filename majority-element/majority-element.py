class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #solved using Boyer-Moore Voting algorithm
        count = 0
        target = None
        for num in nums:
            if(count == 0):
                target = num
            
            if(target == num):
                count += 1
            else:
                count -= 1
        
        return target