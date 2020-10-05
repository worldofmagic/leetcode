#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        n_list = [str(i) for i in range(1,n+1)]
        for i in range(2,n,3):
            n_list[i] = "Fizz"
        for i in range(4,n,5):
            n_list[i] = "Buzz"
        for i in range(14, n, 15):
            n_list[i] = "FizzBuzz"
        return n_list
# @lc code=end

