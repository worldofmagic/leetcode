#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     left, right = 0,0
    #     while right < len(nums):
    #         if nums[right] != 0:
    #             if left != right:
    #                 nums[left] = nums[right]
    #             left += 1
    #         right += 1

        
    #     while left < len(nums):
    #         if nums[left] != 0:
    #             nums[left] = 0
    #         left += 1
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums) - 1
        zeros = []
        while n >= 0:
            if nums[n] == 0:
                nums.pop(n)
                zeros.append(0)
            n -= 1
        nums.extend(zeros)

  

        
# @lc code=end

