#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start


class Solution:
    count = 0
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_len = len(digits)
        result = [0]*digits_len
        for n,i in enumerate(digits[::-1]):
            if(n == 0):
                add_sum = self.count + i + 1
            else:
                add_sum = self.count + i
            self.count = 0
            curr = add_sum % 10
            self.count = add_sum //10
            result[n] = curr
            print(self.count)
            if n == digits_len - 1 and self.count != 0:
                result.append(self.count)

            
        return result[::-1]

        
# @lc code=end

