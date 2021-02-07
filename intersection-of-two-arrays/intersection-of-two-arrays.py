class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Time: O(n + m)
        #Space: O(n + m)
        
        table = {}
        
        for num in nums1:
            if num not in table:
                table[num] = True
        
        res = []
        for num in nums2:
            if num in table and table[num] == True: #only get nums once
                res.append(num)
                table[num] = False
                
        return res