class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Time = Space = O(4^n / root n). 
        ans = []
        
        def backtrack(list=[], left = 0, right=0):
            if len(list) == 2 * n:
                ans.append(''.join(list))
                return
            if left < n:
                list.append('(')
                backtrack(list, left + 1, right)
                list.pop()
            if right < left:
                list.append(')')
                backtrack(list, left, right + 1)
                list.pop()
        backtrack()
        return ans