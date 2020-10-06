#
# @lc app=leetcode id=475 lang=python3
#
# [475] Heaters
#

# @lc code=start
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
         # Write your code here
        heaters.sort()
        ans = 0
        for house in houses:
            ans=max(ans,self.closestHeater(house,heaters))
        return ans
        
    def closestHeater(self,house,heaters):
        start = 0
        end = len(heaters) - 1
        while start + 1 < end:
            m = start + (end - start) // 2
            if heaters[m] == house:
                return 0
            elif heaters[m] < house:
                start = m
            else:
                end = m
        return min(abs(house - heaters[start]), abs(heaters[end] - house))


        
# @lc code=end

