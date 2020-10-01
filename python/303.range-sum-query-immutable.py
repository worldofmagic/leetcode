#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = [0]
        for i in nums:
            self.sum.append(self.sum[-1] + i)
        

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1] - self.sum[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

