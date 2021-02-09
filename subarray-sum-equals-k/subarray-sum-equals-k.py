class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        counter = 0
        table = {}
        
        table[0] = 1
        
        for num in nums:
            running_sum += num

            if running_sum - k in table:
                counter += table[running_sum - k]
            
            table[running_sum] = table[running_sum] + 1 if running_sum in table else 1
                    
        return counter
                