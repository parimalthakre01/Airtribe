# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1 - [Himanshu (Airtribe)]

# https://leetcode.com/problems/maximum-average-subarray-i/description/ - [Himanshu (Airtribe)]

# https://github.com/himanshubuyerteam/July_DSA_Batch.git - [Himanshu (Airtribe)]


# SLIDING WINDOW 

# Brute Force Approach 
# Given an array with the size n and sub array size k. Find the sub array with max sum 

class Solution:
    def getMaxSum(self, nums, m : int):
        max_sum = 0
        sub_sum = 0
        for i in range(0, len(nums)-m):
            for j in range(i, i + m):
                sub_sum += nums[j]
                print(f"Sub sum: {sub_sum}, j : {j}")
                if sub_sum > max_sum: 
                    max_sum = sub_sum    
            sub_sum = 0        
        return max_sum
    
    def getMaxSumOptimized(self, nums, m:int):
        max_sum = 0
        i = m-1
        curr_sum = sum(nums[:m])
        max_sum = curr_sum
        for i in range(m, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i-m]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    
sol = Solution()
res = sol.getMaxSum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
res2 = sol.getMaxSumOptimized([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)
print(res)
print(res2)