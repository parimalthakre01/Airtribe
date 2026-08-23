# BINARY ARRAY SORTING 

# [0, 0, 1, 0, 1, 0, 0, 1, 1] -> [0 , 0, 0, 0, 0, 1, 1, 1, 1]

class binaryArray: 
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def sortBinaryArray(self, nums): 
        i = 0 
        j = len(nums) - 1
        
        while(i<j):
            if nums[i] == 0 and nums[j] == 1:
                i += 1
                j -= 1
            elif nums[i] == 0 and nums[j] == 0:
                i += 1
            elif nums[i] == 1 and nums[j] == 0:
                self.swap(nums, i, j)
                i += 1
                j -= 1
        return nums
    
obj = binaryArray()

res = obj.sortBinaryArray([0, 0, 1, 0, 1, 0, 0, 1, 1])
print(res)