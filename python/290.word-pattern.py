#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        str_to_pa = {}
        pa_to_str = {}

        match = True

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            pattern_char = pattern[i]
            word = words[i]

            if pattern_char not in pa_to_str:
                pa_to_str[pattern_char] = word
            elif pa_to_str[pattern_char] != word:
                match = False
                break

            if word not in str_to_pa:
                str_to_pa[word] = pattern_char
            elif str_to_pa[word] != pattern_char:
                match = False
                break

        print(str_to_pa)
        print(pa_to_str)
        return match
        
# @lc code=end

