#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for i in magazine:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for j in ransomNote:
            if j in count:
                count[j] -= 1
                if count[j] < 0:
                    return False
            else:
                return False
        return True
            
        
# @lc code=end

