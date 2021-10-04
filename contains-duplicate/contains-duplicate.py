class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Time: O(N)
        # Space: O(N)
        # the easiest solution is to just create a map and the first time u see an element that already exists in the map, it must be the duplicate
        
        table = {}
        for elem in nums:
            if elem in table:
                return True
            table[elem] = True
        return False