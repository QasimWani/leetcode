class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #so the idea is to solve this by finding all potential subsets of letter combination given the numbers.
        #first is to find all the subsets for digit[0]. and then find all subset for digit[0] + digit[1].
        #and then continue until we reach the end character. Solving by subproblems. problem is this approach
        #involves a lot of repeated computations. this can be probably avoided since this problem will scale
        #in polynomial time O(2^n). right now, the focus is to get a solution, and optimize later.
        #so, since we're solving for subsets, we need to keep a track of start and end pointers representing
        #digit levels we're at. we append current digit from elements in the range start - end, and once done
        #set start to end, and end to current end position, and repeat this process. we return all the elements
        #from last start thru end. an alternative could be do simply delete all start elements once we're done
        #with one level.
        
        #Time = Space = O(3^n x 4^m) where n and m are the digits that map to 3 and 4 letters in the keypad, repesectively.
        
        if not digits:
            return []
        
        keypad = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'} #load mapping
        
        i = 0 #digit level
        sets = list(keypad[int(digits[i])]) #initialize set
        
        start = 0; end = len(sets)
        i += 1
        while i < len(digits):
            for x in range(start, end):
                for char in list(keypad[int(digits[i])]): #constant 3-4 iterations.
                    sets.append(sets[x] + char)
            start = end
            end = len(sets)
            i += 1
            
        return sets[start:]
