#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = {"q","w","e","r","t","y","u","i","o","p"}
        second = {"a","s","d","f","g","h","j","k","l"}
        third = {"z","x","c","v","b","n","m"}
        res = [word for word in words if set(word.lower()).issubset(first) or set(word.lower()).issubset(second) or set(word.lower()).issubset(third)]
        return res
        
# @lc code=end

