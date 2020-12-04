# Time: O(n^2)
# Space: O(N)
​
class Solution:
    def threeSum(self, array: List[int]) -> List[List[int]]:
        array.sort()
        triplets = set()
        targetSum = 0
        
        sum_map = sum(array)
        #edge case
        if(not array):
            return []
        x = array.count(0)
        if(sum_map == 0 and len(array) == x):
            output = []
            if(x >= 3):
                output.append([0, 0, 0])
            return output
        
        for i in range(len(array) - 2): #-2 for accomodating left and right ptr
            left = i + 1
            right = len(array) - 1
            while(left < right):
                sum_ = array[i] + array[left] + array[right] #x + y + z
                if(sum_ == targetSum):
                    pair = [array[i], array[left], array[right]]
                    pair.sort()
                    triplets.add(tuple(pair))
                    
                    left += 1
                    right -= 1
                elif(sum_ > targetSum):
                    right -= 1
                elif(sum_ < targetSum):
                    left += 1
        return list(triplets)
