class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Time: O(n^2)
        #Space: O(n^2)
        
        n = len(nums)
        nums.sort()
        table = {}
        
        for i in range(n):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                table[a + b] = [[i, j]] if a + b not in table else table[a + b] + [[i , j]]
        
        result = set()
        # a + b = target - (c + d)
        for i in range(n):
            for j in range(i + 1, n):
                c, d = nums[i], nums[j]
                rhs = target - (c + d)
                if rhs in table:
                    for pair in table[rhs]:
                        k, l = pair
                        if len({i, j, k, l}) == 4:#unique indices
                            val = sorted([c, d, nums[k], nums[l]])
                            result.add(tuple(val))
        return list(result)        