class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # since an anagram is multiple representation of the same word, sorting them should produce the same word.
        # so, a group of anagrams should be the same once sorted. so, we can easily group them together based on this key.

        # Time: O(n mlogm), where n is the total number of anagrams and m is the longest anagram
        # Space: O(n) where n is the total number of anagrams
        
        table = {} # key = sorted anagram, value = [original anagram]
        
        for gram in strs:
            sg = "".join(sorted(gram))
            if sg in table:
                table[sg].append(gram)
            else:
                table[sg] = [gram]
        
        
        return table.values()