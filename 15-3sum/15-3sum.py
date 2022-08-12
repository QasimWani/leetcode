# O(n^2) time ; O(n) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        table = {nums[i] : i for i in range(len(nums))}
        
        sol = set()
        for i in range(len(nums)):
            a = nums[i]
            for j in range(i, len(nums)):
                b = nums[j]
                if -(a + b) in table:
                    k = table[-a - b]
                    if i != j and i != k and j != k:
                        answer = sorted([a, b, -a - b])
                        sol.add(tuple(answer))
        return list(sol)