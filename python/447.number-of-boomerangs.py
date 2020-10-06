#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#

# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        distance = lambda a, b : (a[0]-b[0])**2 + (a[1]-b[1]) **2
        
        total = 0
        for a in points:
            dist = {}
            for b in points:
                dis = distance(a,b)
                if dis in dist:
                    dist[dis] += 1
                else:
                    dist[dis] = 1
            for count in dist.values():
                total += count * (count -1)
        return total

        
# @lc code=end

