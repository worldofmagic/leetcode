#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        p1 = 0
        p2 = len(s)-1
        s_arr = list(s)
        while p1 <= p2:
            if s_arr[p1] in vowels and s_arr[p2] in vowels:
                s_arr[p1], s_arr[p2] = s_arr[p2], s_arr[p1]
                p1+=1
                p2-=1
            elif s_arr[p1] not in vowels and s_arr[p2] in vowels:
                p1+=1
            elif s_arr[p1] in vowels and s_arr[p2] not in vowels:
                p2-=1
            else:
                p1+=1
                p2-=1
        return "".join(s_arr)


        
# @lc code=end

