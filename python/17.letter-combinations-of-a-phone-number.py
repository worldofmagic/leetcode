#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    keyboard = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        results = []
        self.dfs(digits,0,[],results)
        return results
    
    def dfs(self, digits, index, chars, results):
        if index == len(digits):
            results.append("".join(chars))
            return
        
        for letter in self.keyboard[digits[index]]:
            chars.append(letter)
            self.dfs(digits, index+1,chars, results)
            chars.pop()


        
        
# @lc code=end

