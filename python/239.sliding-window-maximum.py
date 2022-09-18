#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
import collections

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = collections.deque()
        res = []
        for i, num in enumerate(nums):
            if que and i-que[0][0]>=k:
                que.popleft()
            while que and que[-1][1] <=num:
                que.pop()
            que.append([i, num])
            if i>= k-1:
                res.append(que[0][1])
        return res




    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     l = len(nums)
    #     res = []
    #     for i in range(l+1-k):
            
    #     res = [max(nums[i:i+k]) for i in range(l+1-k)]
    #     return res
        
# @lc code=end

