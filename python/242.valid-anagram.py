#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = [0] * 256
        set_t = [0] * 256
        for i in range(0, len(s)):
            set_s[ord(s[i])] += 1
        for i in range(0, len(t)):
            set_t[ord(t[i])] += 1
        for i in range(0, 256):
            if set_s[i] != set_t[i]:
                return False
        return True

        
# @lc code=end

