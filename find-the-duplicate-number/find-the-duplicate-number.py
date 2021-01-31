class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #sort numbers and find the instance where nums[i] == nums[i + 1], and return that number
        #Space: O(1)
        #Time: O(nlogn)
        nums.sort()
        for i in range(1, len(nums)):
            if(nums[i - 1] == nums[i]):
                return nums[i]
        return -1