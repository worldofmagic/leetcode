#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator % denominator == 0:
            return str(numerator // denominator)

        sign = "-" if numerator // denominator < 0 else ""
        num, den = abs(numerator), abs(denominator)

        n, rem = divmod(num, den)
        res = sign + str(n) + "."
        
        print("n is {} and rem is {}".format(n, rem))
        #纪录 rem 对应的位置
        num_to_pos = {}

        while rem and rem not in num_to_pos:
            num_to_pos[rem] = len(res)
            n, rem = divmod(10 * rem, den)
            res += str(n)

        if rem in num_to_pos:
            #如果rem重复，在对应的位置 插入 "("
            index = num_to_pos[rem]
            res = res[:index] + "(" + res[index:] + ")"

        return res  
# @lc code=end

