#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
            else:
                if dict1[s[i]] != t[i]:
                    return False
            if t[i] not in dict2:
                dict2[t[i]] = s[i]
            else:
                if dict2[t[i]] != s[i]:
                    return False
                    
        return True



        
# @lc code=end

