#Time: O(n)
#Space: O(n)
class Solution:
    def twoSum(self, nums, target):
        table = {}
        # x + y = target
        for i, num in enumerate(nums):
            if target - num in table:
                return table[target - num], i # target - num in table
            table[num] = i
            
        return None