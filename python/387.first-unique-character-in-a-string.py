#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1

        print(counter)
        for c in s:
            if counter[c] == 1:
                return s.index(c)
        return -1


        
# @lc code=end

