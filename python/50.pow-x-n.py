#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x, n):
        # Take care of the case when n < 0    
        if n < 0:
            x = 1/x 
            n = -n
        
        ans = 1 
        current_product = x
        while n > 0:
            if n % 2 == 1:
                ans = ans * current_product
                n = n-1
            else:
                # when the power is even, double the current product, (e.g. 2^4 = (2^2)^2)
                current_product = current_product * current_product
                n = n // 2
        return ans
        
# @lc code=end

