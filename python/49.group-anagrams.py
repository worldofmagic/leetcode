#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

import collections

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            res[sorted_str].append(string)
        return res.values()
        
# @lc code=end

