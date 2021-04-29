#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start


class Solution:
    def calculate(self, s: str) -> int:
        result_stack = []
        result = 0
        number = 0
        sign = 1
        for c in s:
            if c in '0123456789':
                number = number * 10 + int(c)
            elif c == '+':
                result += sign*number
                number = 0
                sign = 1
            elif c == '-':
                result += sign*number
                number = 0
                sign = -1
            elif c == '(':
                result_stack.append(result)
                result_stack.append(sign)
                sign = 1
                result = 0
            elif c == ')':
                result += sign*number
                number = 0
                result *= result_stack[-1]
                result += result_stack[-2]
                result_stack = result_stack[0:-2]
        result += sign * number
        return result
        
                    


            # @lc code=end
