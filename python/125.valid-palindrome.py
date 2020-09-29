#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        char_arr = [char for char in s if char.isalnum()]
        i, j = 0, len(char_arr)-1
        while i<j:
            if char_arr[i]!= char_arr[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
        
        
# @lc code=end

