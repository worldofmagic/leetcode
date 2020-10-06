#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        sumNum = sum(nums)
        minNum = min(nums)
        return sumNum - minNum * len(nums)

# 让我们定义 sum 为移动前数组中所有元素的和； minNum 为数组中最小的元素值； n 是数组的长度
# 那么，在 m 次移动操作后，我们得到了数组的元素为 x （此时数组中的元素已经全部相等），于是我们可以得到这么一个关系：
# sum + m * (n - 1) = x * n
# 实际上：
# x = minNum + m
# 最后，我们能够得到这么一个关系式：
# sum - minNum * n = m
# 所以现在这个问题非常简单了
# @lc code=end

