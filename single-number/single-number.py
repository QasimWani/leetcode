class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #take xor of all bits. A XOR 0 = A, A XOR A = 0. 
        # A XOR B XOR A = (A XOR A) XOR B = 0 XOR B = B.
        result = nums[0]
        for num in nums[1:]:
            result ^= num
        return result
            
            