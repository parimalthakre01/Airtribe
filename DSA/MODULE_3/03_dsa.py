# RSA -> Rotated Sorted Array 
# Given a RSA find the minimum element in RSA 

# [2, 5, 7, 12, 18, 20] -> [20, 2, 5, 7, 12, 18] -> [18, 20, 2, 5, 7, 12]

class Solution():
    def binarySearchRSA(self, arr):
        self.arr = arr
        
        lenArray = len(arr)
        s = 0
        e = lenArray - 1
        mid = 0
        while s < e: 
            mid = s + (e-s)//2
            
            if arr[mid] > arr[e]:
                s = mid+1
            else: 
                e = mid
                
        return arr[s]
    
    def findNumberOfRotation(self, arr):
        self.arr = arr
        lenArray = len(arr)
        
        s = 0
        e = lenArray - 1
        while s<e:
            mid = s + (e-s)//2
            
            if arr[mid] > arr[e]:
                s = mid+1
            else:
                e = mid
            
        return s
    
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
    
    def findTargetInRSA(self, arr, target):
        rotation = self.findNumberOfRotation(arr)
        
        # get two RSAs 
        RSA1 = arr[0:rotation]
        print(RSA1)
        RSA2 = arr[rotation: len(arr)]
        print(RSA2)
        # apply bs on RSA1 and RSA2 
        bs1 = self.binarySearchFirstOccurance(RSA1, target)
        bs2 = self.binarySearchFirstOccurance(RSA2, target)
        
        if bs1:
            return bs1
        else:
            return bs2
        
sol = Solution()
# ans = sol.binarySearchRSA([18, 20, 2, 5, 7, 12])
# numOfRotations = sol.findNumberOfRotation([3, 9, 7, 1, 2])
# print(numOfRotations)
# print(ans)

ele = sol.findTargetInRSA([12, 20, 25, 40, 1, 5, 8 , 10] , 40)
print(ele)