#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c in {"(", "[", "{"}:
                    stack.append(c)
                else:
                    top = stack.pop()
                    if check.get(top) != c:
                        return False
        return not stack

        # @lc code=end
