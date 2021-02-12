class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #get new S and T and compare is new S = new T
        s = list(S[0]) if S[0] != '#' else []
        t = list(T[0]) if T[0] != '#' else []
        
        
        i = len(s)
        for char in S[1:]:
            if char == '#' and s:
                i -= 1
                s.pop(i)
            elif(char != '#'):
                s.append(char)
                i += 1
                
        i = len(t)
        for char in T[1:]:
            if char == '#' and t:
                i -= 1
                t.pop(i)
            elif(char != '#'):
                t.append(char)
                i += 1

        return s == t
        