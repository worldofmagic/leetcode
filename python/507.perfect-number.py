#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # divisors = [i for i in range(1, num) if num % i ==0]
        divisors = set()
        for i in range(1, math.floor(math.sqrt(num)) + 1):
            if i in divisors:
                continue
            if num % i == 0:
                divisors.add(i)
                divisors.add(num//i)
        if num in divisors:
            divisors.remove(num)
        return sum(divisors) == num
        
# @lc code=end

