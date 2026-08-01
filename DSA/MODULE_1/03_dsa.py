# BALANCE POINT/ EQUILIBRIUM POINT/ PIVOT POINT

# https://leetcode.com/problems/find-pivot-index/description/

# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

 

# Example 1:

# Input: nums = [1,7,3,6,5,6]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11


# solution
from typing import List

class Solution:
    # def __init__(self, nums: List[int]):
    #     self.arr = nums
        
    # brute force
    def pivotIndex(self, nums: List[int]) -> int:
        self.arr = nums

        for i in range(0, len(nums)):
            left_sum = 0
            right_sum = 0
            for j in range(0, i):
                left_sum += nums[j]
            
            for k in range(i+1, len(nums)):
                right_sum += nums[k]

            if left_sum == right_sum:
                return i
        return -1
    
    def optimizedPivotIndex(self, nums : List[int]) -> int:
        self.arr = nums
        psum = [0]*len(nums)

        psum[0] = nums[0] 
        for i in range (1, len(nums)):
            psum[i] = psum[i-1] + nums[i]
        
        for i in range (0, len(nums)):
            if  i == 0:
                left_sum = 0
                right_sum = psum[len(nums)-1] - psum[0]
            else:
                left_sum = psum[i-1]
                right_sum = psum[len(nums)-1] - psum[i]
            
            if left_sum == right_sum:
                return i    
        return -1


obj = Solution() 
sol = obj.pivotIndex([1,7,3,6,5,6])         
sol2 = obj.optimizedPivotIndex([1,7,3,6,5,6])
print(sol)              
print(sol2)