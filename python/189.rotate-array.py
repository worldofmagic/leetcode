#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Write your code here
        length = len(nums)
        k = k % length
        for i in range(k):
            temp = nums.pop()
            nums.insert(0, temp)


# @lc code=end

