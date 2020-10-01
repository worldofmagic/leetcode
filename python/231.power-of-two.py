#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      # Write your code here
        if (n <= 0) :
            return False
        return (n & (n-1)) == 0
        
# @lc code=end

