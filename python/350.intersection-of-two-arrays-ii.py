#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = sorted(nums1)
        s2 = sorted(nums2)
        i, j = 0, 0
        result = []
        while i < len(s1) and  j < len(s2):
            if s1[i] == s2[j]:
                result.append(s1[i])
                j+=1
                i+=1
            elif s1[i] < s2[j]:
                i += 1
            elif s1[i] > s2[j]:
                j += 1
        return result
        
# @lc code=end

