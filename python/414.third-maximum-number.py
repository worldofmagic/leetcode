#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        ans = [-float('inf')]*3
        for i in nums:
            if i > ans[0]:
                ans.insert(0, i)
                ans.pop(-1)
            elif ans[0] > i > ans[1]:
                ans.insert(1, i)
                ans.pop(-1)
            elif ans[1] > i > ans[2]:
                ans.insert(2, i)
                ans.pop(-1)
            print(ans)
        if ans[2] > -float('inf'):
            return ans[2]
        if ans[0] > -float('inf'):
            return ans[0]
        else:
            return -1

# @lc code=end
