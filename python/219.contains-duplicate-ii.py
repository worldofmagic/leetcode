#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for index, value in enumerate(nums):
            print(dic)
            if value in dic and index - dic[value] <= k:
                return True
            dic[value] = index
        return False
        
# @lc code=end

