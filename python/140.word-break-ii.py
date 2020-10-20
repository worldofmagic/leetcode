#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.dfs(s,wordDict,{})
    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
            
        if len(s) == 0:
            return []
            
        partitions = []
        
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            
            sub_partitions = self.dfs(s[i:], wordDict, memo)
            for partition in sub_partitions:
                partitions.append(prefix + " " + partition)
                
        if s in wordDict:
            partitions.append(s)
            
        memo[s] = partitions
        return partitions

        
# @lc code=end

