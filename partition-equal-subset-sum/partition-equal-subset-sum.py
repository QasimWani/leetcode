class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #this can be solved using a 0/1 Knapsack problem formulation.
        #We can prove that the partition value for each array can only be equal to 
        #the half of sum of the entire array, i.e. if partition is possible.
        #this is because ∑ partition_one = ∑ partition_two, which is given.
        #This further implies that elements in partition_one & partition_two = {nums}.
        
        #To formulate it as knapsack problem:
        #Max-weight = 1/2 ∑ nums[i].
        #item value = item weight. So, to if the last cell = last cell's weight, return true.
        #This is because, the max sum cannot be > last weight because the value at each cell
        #corresponds to its weight. Therefore, the max possible sum of values must be less than
        #or equal to last cell's weight. If its equal, return true; else return false.
        #Since this is a standard Knapsack problem, time = space = O(n * m),
        #where m = number of weights and n = number of values. Here m = 1/2 ∑ nums[i].
        #and n = len(nums).
        
        m = sum(nums) / 2
        
        if(m != int(m)): #if half is a fraction, no partition of integers can generate that result
            return False
        
        m = int(m) #typecast to int [optional]
        grid = [[0 for _ in range(m + 1)] for _ in nums]
        
        ### Knapsack algorithm
        # v[i, w] = max( v[i - 1, w], v[i - 1, w - w[i]] + p[i] )
        
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                grid[i][j] = max( grid[i - 1][j] , grid[i - 1][j - nums[i]] + nums[i] if j - nums[i] >= 0 else grid[0][0])
                if(grid[i][j] == m): #half found, terminate early.
                    return True
                
        return False     
