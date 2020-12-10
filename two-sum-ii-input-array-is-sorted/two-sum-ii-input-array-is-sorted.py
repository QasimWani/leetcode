class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, second = 0, len(numbers) - 1
        while(first < second):
            if(numbers[first] + numbers[second] == target):
                return [first + 1, second + 1]
            elif(numbers[first] + numbers[second] < target):
                first += 1
            else:
                second -= 1
​
