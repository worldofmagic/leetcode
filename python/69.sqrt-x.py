#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            return None
        start, end = 0, x
        while start+1< end:
            mid = start + (end - start)//2
            if mid * mid <= x:
                start = mid
            else:
                end = mid
        if end * end <= x:
            return end
        return start
        
# @lc code=end

