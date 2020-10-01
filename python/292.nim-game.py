#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

# class Solution:
#     def canWinBash(self, n):
#         return self.memo_search(n, {})

#     def memo_search(self, n, memo):
#         if n <= 3:
#             return True
#         if n in memo:
#             return memo[n]
#         for i in range(1, 4):
#             if not self.memo_search(n - i, memo):
#             # 若后续状态有必败态，则当前为必胜态
#                 memo[n] = True
#                 return True
#         memo[n] = False
#         return False
# @lc code=end

