#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
                # write your code here
        if n <= 1:
            return 0
        res = 0
        not_prime = [False] * n
        for i in range(2, n):
            if not_prime[i] == False:
                res += 1
                for j in range(2, n):
                    if j * i >= n:
                        break
                    not_prime[j * i] = True
        return res
        
# @lc code=end

