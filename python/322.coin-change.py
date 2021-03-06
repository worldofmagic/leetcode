#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: 
                return memo[n]
            # base case
            if n == 0: 
                return 0
            if n < 0: 
                return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: 
                    continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)
        
# @lc code=end

