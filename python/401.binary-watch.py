#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        ans = []
        hour = [[], [], [], []]
        minute = [[], [], [], [], [], []]
        for i in range(0, 12):
            n = bin(i).count('1')
            hour[n].append(i)
        for i in range(0, 60):
            n = bin(i).count('1')
            minute[n].append(i)
        for i in range(0, num + 1):
            if i < 4 and num - i < 6:
                for h in hour[i]:
                    for m in minute[num - i]:
                        ans.append('%d:%02d' % (h, m))
        return ans
# @lc code=end

