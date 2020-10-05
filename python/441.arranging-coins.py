#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 0:
            return n
        start, end = 0, n
        while start + 1 < end:
            mid = start + (end - start)//2
            if mid * (mid+1) //2 <= n: 
                start = mid
            else:
                end = mid
        if end*(end+1)//2 <= n: 
            return end
        if start * (start+1) //2 <= n:
            return start
    # return math.floor((-1 + math.sqrt(1 + 8*n)) / 2)
        
# @lc code=end

