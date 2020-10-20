#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        
        n= len(s)
        dp = [False]*(n+1)
        dp[0] = True
        max_length = max([len(word) for word in wordDict]) if  wordDict else 0

        for i in range(1, n+1):
            for l in range(1, max_length+1):
                if i < l :
                    break
                if not dp[i-l]:
                    continue
                word = s[i-l:i]
                if word in wordDict:
                    dp[i] = True
                    break
                
        return dp[n]
        
# @lc code=end

