class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        
        current_sum = 0
        left_ptr = 0
        min_dist = float('inf')
        
        for i in range(len(nums)):
               
            current_sum += nums[i]
            
            while current_sum >= target:
                min_dist = min(min_dist, i - left_ptr + 1)
                current_sum -= nums[left_ptr]
                left_ptr += 1

        
        return min_dist if min_dist != float('inf') else 0