# http://leetcode.com/problems/koko-eating-bananas/description/


# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.

# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30


class Solution():
    
    # Is possible to eat all the piles with Speed within hr
    def isPossbileToEat(self, piles, speed, h):
        total_hours = 0
        
        for i in range(len(piles)):
            if piles[i] % speed == 0:
                total_hours = total_hours + piles[i]/speed
            else:
                total_hours = total_hours + piles[i]//speed + 1
                
        if total_hours > h:
            return False
        
        return True
        
    def minEatingSpeed(self, piles, h):
        self.piles = piles
        self.h = h
        
        s  = 1
        e = max(piles)
        possible_ans = e
        
        while (s<=e):
            mid = s + (e-s)//2
            if self.isPossbileToEat(piles, mid, h):
                possible_ans = mid
                e = mid-1
            else:
                s = mid+1
        return possible_ans
            
sol = Solution()
res = sol.minEatingSpeed([3,6,7,11], 8)
print(res)