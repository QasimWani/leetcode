class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #so basically create a counter using dict of all words and then store it in a heap and pop k elements.
        #Time: O(N log K)
        #Space: O(N)
        
        table = {}
        for word in words:
            if(word in table):
                table[word] -= 1
            else:
                table[word] = -1
                
        heap = [(freq, word) for word, freq in table.items()]
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]