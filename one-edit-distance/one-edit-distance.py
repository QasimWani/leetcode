class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        #quite simple solution. because we're checking for one edit distance, the assumption is that the length of s is at most 1 unit away from t.
        #this means that s is either equal to t or is less than or greater than t by a length of 1.
        #if they're of the same length and there exists a character where the 2, s and t, are different. then we need to check equivalence of the
        #two strings excluding that character.
        #however, if the two strings are of 2 different lengths, then we need to check if removing that character from the string of greater length
        #makes the 2 strings identical.
        
        #Time: O(N)
        #Space: O(1)
        
        if len(s) < len(t): #to make things easier, we assume s is always >= t
            s, t = t, s #swap
        
        len_s, len_t = len(s), len(t)
        
        if len_s - len_t >= 2: #underlying base condition
            return False
        
        for i in range(len_t):
            if s[i] != t[i]:
                #if the strings are of equal length, check if remainder of characters are equal to one another
                if len_s == len_t:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:]
                
        return len_s - len_t == 1 #since they need to be one distance apart, we just check if the diff. between them is 1.
                    