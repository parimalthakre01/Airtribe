# Two SUM 

# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSumBruteForce(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
                    
        return output
    
    # only for sorted array
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums)-1
        while(i < j):
            curr_sum = nums[i] + nums[j]
            if curr_sum == target:
                return [i+1, j+1]
            elif curr_sum > target: 
                j -= 1
            else:
                i += 1

        return [-1,-1]
obj = Solution()
ans = obj.twoSum([3,2,4], 6)
print(ans)