class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Greedy solution. Don't even need to maintain a DP table.
        #Time: O(n)
        #Space: O(1)
        
        last_pos = nums[0]
        
        for i in range(1, len(nums)):
            last_pos = max(last_pos, nums[i - 1]) - 1
            if last_pos < 0:#no possible way to continue
                return False
        return last_pos >= 0