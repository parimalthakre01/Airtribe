# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Brute Force Approach 
from typing import List
class Solution: 
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        ansLen = float('inf')
        # currLength = 0
        currSum = 0
        for i in range(len(nums)):
            currSum = currSum + nums[i]
            while currSum >= target:
                currLen = i-j+1
                ansLen = min(currLen, ansLen)
                currSum = currSum - nums[j]
                j = j + 1
        
        return 0 if ansLen == float('inf') else ansLen
            
        
        
sol = Solution()
res = sol.minSubArrayLen([2,3,1,2,4,3], 7)
print(res)