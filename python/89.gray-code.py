#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [int(x, 2) for x in self.dfs(n)]
        
    def dfs(self,n):
        if n==0:
            return ['0']
        elif n==1:
            return ['0','1']
        else:
            nums = self.dfs(n-1)
            return ['0' + num for num in nums] + ['1' + num for num in nums[::-1]]
        


    # def grayCode(self, n: int) -> List[int]:
    #     grays = dict()
    #     grays[0] = ['0']
    #     grays[1] = ['0','1']
    #     for i in range(2, n+1):
    #         n_gray = []
    #         for pre in grays[i-1]:
    #             n_gray.append('0'+pre)
    #         for pre in grays[i-1][::-1]:
    #             n_gray.append('1'+pre)
    #         grays[i] = n_gray
    #     return map(lambda x: int(x, 2), grays[n])
        
# @lc code=end

