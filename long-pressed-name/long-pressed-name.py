class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):#not all characters were typed
            return False
        
        #basically run a run-length encoding for name and typed and compare whether 
        #each frequency of typed is greater than or equal to associated name character
        name = self.encode(name)
        typed = self.encode(typed)
        if len(name) != len(typed):
            return False
        
        for x, y in zip(name, typed):
            if x[1] == y[1] and y[0] >= x[0]:
                continue
            else:
                return False
        return True
        
    def encode(self, string):
        arr = []
        for char in string:
            if(not arr or arr[-1][1] != char):
                arr.append([1, char])
            else:
                counter = arr[-1][0] + 1
                arr[-1] = [counter, char]

        return arr