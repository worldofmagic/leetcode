#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num ==0 or num ==1:
            return True
        start, end = 0, num
        while start + 1 < end:
            mid = start + (end - start)//2
            if mid*mid < num:
                start = mid
            else:
                end = mid
        if start*start == num:
            return True
        if end*end == num:
            return True
        return False
# @lc code=end

