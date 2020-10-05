#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length = max(len(num1), len(num2))
        carry = 0
        res = []
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(length):
            a = int(num1[i]) if i < len(num1) else 0
            b = int(num2[i]) if i < len(num2) else 0
            temp_sum = a + b + carry
            carry = temp_sum // 10
            cur = temp_sum % 10
            print("a is {}, b is {}, temp_sum is {}, carry is {}, cur is {}".format(a, b, temp_sum, carry, cur))
            res.append(cur)
            if i == length - 1 and carry != 0:
                res.append(carry)
        print(res)
        return "".join(map(str, res[::-1]))
# @lc code=end

