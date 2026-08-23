# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        left_ch = s[i]
        right_ch = s[j]
        while i<j:
            if left_ch.isalnum():
                i += 1
            elif right_ch.isalum():
                j -= 1
            else:
                if left_ch.lower() != right_ch.lower():
                    return False
            i += 1
            j -= 1
        return True
    
obj = Solution()
result = obj.isPalindrome("A man, a plan, a canal: Panama")
print(result)