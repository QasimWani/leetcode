class Solution:
    def removeDuplicates(self, S: str, i=0) -> str:
        # recursively remove adjacent characters until no adjacent & equal characters are to be found.

        i = 0
        l = len(S)
        flag = False
        while i < l - 1:
            if S[i] == S[i + 1]:
                flag = True
                S = S[:i] + S[i + 2 :]
                l -= 2
            i += 1
        
        return S if not flag else self.removeDuplicates(S)