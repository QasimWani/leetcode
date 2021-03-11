class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        #Palindrome if and only if the characters on the left are equal to the right.
        #there's 2 cases for a palindrome: 1) split on a character, 2) split across an index, not a character.
        #example (1): aba. split at b.
        #example (2): abba. split between the 2 b's. ab = reverse(ba)
        #so, a string being a palindrome if either there exists a character with odd frequency and everything else being an even frequency.
        #or, all character frequencies are even (ex. racecar).
        
        #Time: O(N), where n is the length of the string, s
        #Space: O(1). note that the maximum capacity is bounded by ASCII/unicode, so it's technically constant space.
        
        table = {}
        for char in s:
            if char in table:
                table[char] += 1
            else:
                table[char] = 1
        
        odd_counter = 0
        even_counter = 0
        
        for char in table:
            if table[char] % 2 == 0:
                even_counter += 1
            else:
                odd_counter += 1
                
        #case 1: all character even, i.e. number of unique characters == even_counter
        #case 2: all but 1 character frequencies even.
        if len(table) == even_counter or odd_counter == 1:
            return True
        
        return False