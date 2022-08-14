class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams sorted are equal. if multiple substrings sorted are equal, group them together.
        # Time: O(n log n) # time taken to sort anagram. here n refers to longest anagram
        # Space: O(n) # all the substrings
        anagrams = {}
        
        for char in strs:
            aga = "".join(sorted(char))
            if aga in anagrams: # already exists, keep appending
                anagrams[aga].append(char)
            else:
                anagrams[aga] = [char]
        return list(anagrams.values())