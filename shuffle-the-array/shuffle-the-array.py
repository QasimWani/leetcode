class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = []
        for i in range(n):
            arr.append(nums[i])
            arr.append(nums[n + i])
        return arr
        