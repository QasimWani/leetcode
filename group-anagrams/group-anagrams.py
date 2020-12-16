class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Since anagrams deal with words with different positions but same
        # characters, sorting each anagram would produce equivalent words.
        # From sorting the words, we can simply build a hashtable and append
        # words to the correct anagram based on its sorted value.
​
        table = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if(sorted_word in table):
                table[sorted_word].append(word)
            else:
                table[sorted_word] = [word]
        return list(table.values())
