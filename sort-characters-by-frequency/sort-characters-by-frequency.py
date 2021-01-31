class Solution:
    def frequencySort(self, s: str) -> str:
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

        