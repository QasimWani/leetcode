class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #get new S and T and compare is new S = new T
        #Time: O(n + m), where n = len(S) and m = len(T)
        #Space: O(n + m)
        def solve(X):
            x = list(X[0]) if X[0] != '#' else []
            i = len(x)
            for char in X[1:]:
                if char == '#' and x:
                    i -= 1
                    x.pop(i)
                elif(char != '#'):
                    x.append(char)
                    i += 1
            return x
        
        return solve(S) == solve(T)
        