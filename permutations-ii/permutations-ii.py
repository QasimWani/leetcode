class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.helper(nums, permutations, [])
        return permutations
    
    def helper(self, nums, answer, curr):
        if(not nums and len(curr)):
            if(curr not in answer):
                answer.append(curr)
        else:
            for i, num in enumerate(nums):
                newArr = nums[:i] + nums[i+1:]
                newCurr = curr + [num]
                self.helper(newArr, answer, newCurr)
        return answer
