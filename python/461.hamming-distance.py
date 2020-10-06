#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = 0

        while(x !=0 or y!=0):
            if(x%2 != y%2):
                distance += 1
            x = x //2
            y = y //2
        return distance
# @lc code=end

