# REVERSE THE ARRAY
from typing import List

class Solution:
    def swap(self, arr : List, i : int, j : int):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
    def reverseArray(self, arr):
        i = 0
        j = len(arr)-1
        while(i<j):
            self.swap(arr, i, j)
        return arr


obj = Solution()
obj.reverseArray([1, 2, 3, 4, 5])