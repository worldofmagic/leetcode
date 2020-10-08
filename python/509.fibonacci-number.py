#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start


class Solution:
    def fib(self, N: int) -> int:
        prev = 0
        cur = 1
        if N == 0:
            return prev
        if N == 1:
            return cur
        i = 2
        while i <= N:
            prev, cur = cur, prev+cur
            i += 1
        return cur
        # if N == 0:
        #     return 0
        # if N == 1:
        #     return 1
        # res = [0] * (N+1)
        # res[0] = 0
        # res[1] = 1
        # for i in range(2, N+1):
        #     print(i)
        #     res[i] = res[i-1] + res[i-2]
        #     print(res[i])
        # return res[N]

# @lc code=end
