class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # extension of 2 sum. compute all possible a,b pairs and store it in a hashtable.
        # then rerun all possible combinations of say c and d such that there exists that value in the hashtable.
        # check that a,b,c,d are distint. if so, append to solution. 
        
        # Time: O(N^2)
        # Space: O(N^2)
        
        map = {}
        count = 0
        for i, a in enumerate(nums):
            for b in nums[i + 1:]:
                key = a * b
                count += map.get(key, 0)
                map[key] = 1 + map.get(key, 0)
                
        return 8 * count
                