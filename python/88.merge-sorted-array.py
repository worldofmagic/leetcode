#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 初始化双指针和当前元素应存储在新数组的位置
        index = m + n - 1
        a = m-1
        b = n-1
        while a>=0 and b>=0:
            if nums1[a] > nums2[b]:
                nums1[index] = nums1[a]
                a -= 1
                index -= 1
            else:
                nums1[index] = nums2[b]
                b -= 1
                index -= 1
        
        while a >= 0:
            nums1[index] = nums1[a]
            a -= 1
            index -= 1
        while  b >= 0:
            nums1[index] = nums2[b]
            b -= 1
            index -= 1
            



# @lc code=end
