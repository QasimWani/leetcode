#Time: O(n)
#Space: O(1)

#Kadane's algorithm is a very simple and intuitive algorithm to solve
#maximum subarray problem.
#> The maximum subarray tasks us to find the maximum sum of a subarray in
#> in an array. For example, array = [1, 3, -4, 2]. In this case, the maximum
#> subarray has a sum of 4, i.e. [1 + 3]. We can solve this problem using
#> Kadane's Algorithm which basically splits the problem into smaller subset of problems.
#> that can be solved using dynamic programming.

#! Here's how it works. 
#<> We know that the subarray of the global sum has to be contiguous in nature (definition of an array).
#<> Therefore, the maximum sum at a specific position, i, is either the previous maximum subarray or the
#<> the current index, i.
#<> To illustrate this, let array = [1, 3, -1, 2].
#<> At index i = 1, the maximum subarray is either the maximum subarray at i = 0 + current position @ i = 1
#<> or just the value at index, i = 1. So, the local max = max(1 + 3, 3). Here, 1 represents the previous local
#<> max, and 1 + 3 represents the extension of the previous subarray. [3] is also a subarray.
#<> Using this approach, we'll have a bunch of local maxima, and the goal is to find a global maxima.
#<> This can be achieved by just comparing the current local max with the previous global max,
#<> global_max = max(local_max, global_max)

#!!! Using this approach, we've condensed search time from O(n^2) {Brute Force}
#!!! to just O(n) with constant space.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #GH COPILOT
        if not nums:
            return 0
        currSum = maxSum = nums[0]
        for num in nums[1:]:
            currSum = max(num, currSum + num)
            maxSum = max(maxSum, currSum)
        return maxSum