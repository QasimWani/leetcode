class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #sliding window solution. start small, and see if the current substr is equal to t. if not, keep moving right pointer
        #when substr == t, we shrink substr by moving left pointer to the right until you no longer satisfy the constraint.
        #when failed, move right pointer and repeat the process. maintain the smallest string.
        
        #Time: O(|S| x |T|)
        #Space: O(|S|) worst case
        
        left, right = 0, 0
        new_trim = ''
        t = list(t)
        
        while right <= len(s):
            if self.present(s[left : right], t):
                if not new_trim:
                    new_trim = s[left : right]
                elif len(s[left : right]) < len(new_trim):
                    new_trim = s[left : right]
                left += 1
            else:
                right += 1
        return new_trim
        
    
    def present(self, str, substr):
        str = collections.Counter(str)
        counter = 0
        for x in substr:
            if x in str and str[x] > 0:
                str[x] -= 1
                counter += 1
        return counter == len(substr)
