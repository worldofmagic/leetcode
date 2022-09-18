#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

import random
# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.position = dict()
        self.nums = list()
        

    def insert(self, val: int) -> bool:
        if val not in self.position:
            self.nums.append(val)
            self.position[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.position:
            idx, last = self.position[val], self.nums[-1]
            self.nums[idx] = last
            self.position[last] = idx
            self.nums.pop()
            self.position.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        index = random.randint(0, len(self.nums)-1)
        return self.nums[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

