# Binary Search  --> only works on the sorted array

# Formula for calculating the MID : M = L + (R-L)//2
# https://www.geeksforgeeks.org/problems/who-will-win-1587115621/1
class Solution():
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
        
    def linearSearch(self, arr, target):
        self.arr = arr
        self.target = target
        
        arrLength = len(arr)
        
        for i in range(0, arrLength):
            if arr[i] == target:
                return i

        return None
    
    def binarySearch(self, arr, target):
        self.arr = arr
        self.target = target
        
        arrLength = len(arr)
        start = 0
        end = arrLength - 1
        
        while(start<= end):
            mid = (start+end)//2
            
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                end = mid-1
            else:
                start = mid + 1
                
        return False
                
    
    def binarySearchIndex(self, arr, target):
        self.arr = arr
        self.target = target
        
        arrLength = len(arr)
        start = 0
        end = arrLength-1
        
        while(start <= end): 
            mid = (start+end)//2 # in production this might break
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                end = mid-1
            else:
                start = mid+1
        
        return None
    
    
            
        
        
    
ans = Solution()
# result = ans.linearSearch([1, 2, 3, 4, 5], 5)
bs = ans.binarySearch([1, 2, 3, 4, 5], 2)
bsi = ans.binarySearchIndex([1, 2, 3, 4, 5], 2)
print(bs)
# print(result)
            