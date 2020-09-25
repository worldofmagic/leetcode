#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0, len(numbers) - 1
        while i < j:
            sum_2 = numbers[i] + numbers[j]
            if sum_2 == target:
                return [i+1,j+1]
            if sum_2 > target:
                j -= 1
            if sum_2 < target:
                i += 1
        return [-1, -1]
        
# @lc code=end

