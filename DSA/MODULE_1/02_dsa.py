# ARRAYS + HASHING 

# PREFIX SUM 

# arr = [2, 3, 4, 1]
# psum = [2, 5, 9, 10]

# https://leetcode.com/problems/range-sum-query-immutable/?envType=problem-list-v2&envId=prefix-sum 

# Question 

# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

from typing import List 

class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.psum = [0]*len(nums)
        
        self.psum[0] == nums[0]
        
        for i in range(1, len(nums)):
            self.psum[i] += self.psum[i-1] + nums[i] 
            

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.psum[right]
        
        return self.psum[right] - self.psum[left-1]
    
    
nums = [-2,0,3,-5,2,-1]
psum_obj = NumArray(nums)
psum_response = psum_obj.sumRange(2, 5)
print(psum_response)
