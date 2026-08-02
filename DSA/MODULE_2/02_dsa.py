# ROTATE AN ARRAY 

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

from typing import List
class Solution:
    def swap(self, nums : List, i : int, j :int):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def rotateBruteForce(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n 
        # [1,2,3,4,5]
        for i in range(k):
            last = nums[n-1] # last = 5
            
            for i in range(n-1, 0, -1): 
                # 1,2,3,4,4
                # 1,2,3,3,4
                # 1,2,2,3,4
                # 1,1,2,3,4
                nums[i] = nums[i-1]
            #5,1,2,3,4
            nums[0] = last
        return nums

    def reverse(self, nums: List[int], i : int, j : int) -> List:
        while(i < j):
            self.swap(nums, i, j)
            i += 1
            j -= 1
        return nums
    
    def rotate(self, nums: List[int], k: int): 
        # reverse entire arr
        k = k % len(nums)
        arr = self.reverse(nums, 0, len(nums)-1)
        
        # reverse the first k elements    
        arr2 = self.reverse(arr, 0, k-1)
        
        # reverse remaining elements
        arr3 = self.reverse(arr2, k, len(nums)-1)
        return arr3

nums = [1,2,3,4,5,6,7]
obj = Solution()
arr = obj.rotate(nums, 3)
print(arr)  

        
        
        
        
