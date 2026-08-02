# Container with most water

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_water = []
        while i != j:
            water = min(height[i], height[j]) * (j-i)
            max_water.append(water)
            if height[i] > height[j]:
                j -= 1 
            else:
                i += 1
        
        return max(max_water)

            
