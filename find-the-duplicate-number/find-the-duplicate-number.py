class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        #solve using pigeonhole principle using Floyd's Tortoise and Hare cycle detection technique.
        tortoise = hare = nums[0]
        
        while True:
            hare = nums[nums[hare]]
            tortoise = nums[tortoise]
            if(hare == tortoise):
                break
                
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare