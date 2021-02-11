class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # so solve this like 2 sum but instead of simply storing just the numbers
        # in a hashset, we'll store the sum of two indices in the set such that
        # the left + right = k.
        
        output = set()
        table = collections.defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                left = target - (nums[i] + nums[j])
                
                if left in table:
                    for key in table[left]:
                        x, y = key
                        if len(set([i, j, x, y])) == 4:
                            values = [nums[i], nums[j], nums[x], nums[y]]
                            values.sort()
                            output.add(tuple(values))
                                
                table[nums[i] + nums[j]].append([i, j])
                
        return output