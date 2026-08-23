# First Occurance 
# Find the first occurace of a Target in the an array


 
class Solution():
    
    # O(n)
    def linearSearch(self, arr, target):
        self.arr = arr 
        self.target = target
        
        arrLength = len(arr)
        for i in range(arrLength):
            if arr[i] == target:
                return i
            
        return None
    
    #O(log n)
    def binarySearchFirstOccurance(self, arr, target):
        self.arr = arr
        self.target = target
        ans  = -1
        arrLength = len(arr)
        
        start = 0
        end = arrLength-1
        while(start <= end):
            mid = start + (end-start)//2
            if arr[mid] == target:
                ans = mid
                end = mid-1
            elif arr[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return ans
                
            
    def binarySearchLastOccurance(self, arr, target):
        self.arr = arr
        self.target = target
        ans  = -1
        arrLength = len(arr)
                
        start = 0
        end = arrLength-1
        while(start <= end):
            mid = start + (end-start)//2
            if arr[mid] == target:
                ans = mid
                start = mid+1
            elif arr[mid] > target:
                end = mid-1
            else:
                start = mid+1
        return ans
    
    def totalOccurances(self, arr, target):
        firstOccurace = self.binarySearchFirstOccurance(arr, target)
        lastOccurance = self.binarySearchLastOccurance(arr, target)
        
        if firstOccurace == -1:
            return 0
        total = lastOccurance - firstOccurace + 1
        return total 
    
cls = Solution()
ans = cls.linearSearch([2,2,3,4,4,3,1,1,1], 4)
ans2 = cls.binarySearchLastOccurance([2,2,3,4,4,3,1,1,1], 4)
ans3 = cls.binarySearchFirstOccurance([2,2,3,4,4,3,1,1,1], 4)

total = cls.totalOccurances([1,1,1,2,2,3,4,4,3], 1)
print(ans2)
print(ans3)
print(total)
# print(ans)