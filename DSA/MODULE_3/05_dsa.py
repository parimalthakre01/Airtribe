# Binary search on Answer

class Solution:
    def getAnswer(self, x):
        self.x = x
        if x == 0:
            return 0
        arr = list[1:x]
        print(arr)

        s = 1
        e = x
        
        while(s<=e):
            mid = s + (e-s)//2
            
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                e = mid-1
            else:
                s = mid+1
                
        return e

sol = Solution()

ans = sol.getAnswer(121)
print(ans)