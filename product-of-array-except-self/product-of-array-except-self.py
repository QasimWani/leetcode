class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #multiply all numbers to find global product. if count(0) > 1, return 0.
        #divide nums[index] with global product to compute final output
        
        zeros = 0
        global_product = 1
        
        for num in nums:
            if(num == 0):
                zeros += 1
            else:
                global_product *= num
        
        if(zeros >= 2):
            return [0]*len(nums)
        
        
        for i in range(len(nums)):
            if(zeros == 1): #all numbers except for index zero = 0
                nums[i] = 0 if nums[i] != 0 else int(global_product)
            else: #no zeros, clean
                nums[i] = int(global_product / nums[i])
        
        return nums
        