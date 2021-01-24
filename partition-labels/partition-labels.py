#Time = O(n)
#Space = O(n)
​
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        #alright, so this seems like a simple multuple pointer problem
        #where i'm basically checking the last index of current element
        #in substring and marking it as closed. I keep doing this dual
        #-pointer swap as long as the last index i'm at is the closed index.
        #when i hit a closed index, i take the first element and compute the
        #length w.r.t last index and move the first index to closed index
        #and reset the closed index. And I continue this process until the
        #end of the array.
        
        arr_set = {} #map each character with first and last index.
        
        #store first and last index of each character in map
        for i, char in enumerate(S):
            if char in arr_set:
                arr_set[char][1] = max(arr_set[char][1], i) #update last char instance
            else:
                arr_set[char] = [i]*2 #set first instance of each character
        
        #at this point, arr_set has a list of first and last instance of each character.
        #now, we need to find the union of all sets.
        first, last = 0, 0
        lengths = [] #objective subarrays
        for num in arr_set.values():
            start, end = num
            if(start >= last): #new bound
                last = end
                first = start
                lengths.append(last - first + 1)
            elif(end > last and start > first): #new ending point
                last = end
                lengths[-1] = last - first + 1
        
        return lengths
