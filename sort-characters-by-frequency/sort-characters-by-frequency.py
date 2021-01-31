class Solution:
    def frequencySort(self, s: str) -> str:
        #Space: O(n)
        #Time: O(mlogm), where m is the number of unique characters. worst case, m = n, i.e O(n log n).
        
        #The idea is simple: geet the frequency distribution of all characters in s. then use a heap to get the most frequent character
        #and then pop it and append to final result with its multiple of frequency.
        
        table = {}
        for char in s:
            table[char] = table[char] + 1 if(char in table) else 1
        
        heap = [(-freq, character) for character, freq in table.items()]
        
        heapq.heapify(heap)
        
        result = ''
        while(len(heap) > 0):
            f, c = heapq.heappop(heap)
            result += c * abs(f)
        
        return result