#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # if word.islower():
        #     return True
        # if word.isupper():
        #     return True
        # if str(word[0]).isupper() and str(word[1:]).islower():
        #     return True
        # return False
        count_upper = 0
        for c in word:
            if 'A' <= c <= 'Z':
                count_upper += 1
        
        if count_upper == 0:
            return True
        if count_upper == 1 and 'A' <= word[0] <= 'Z':
            return True
        if count_upper == len(word):
            return True
        return False
        
# @lc code=end

