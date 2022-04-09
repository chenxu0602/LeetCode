#
# @lc app=leetcode id=2169 lang=python3
#
# [2169] Count Operations to Obtain Zero
#

# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        return 0 if num1 * num2 == 0 else num1 // num2 + self.countOperations(num2, num1 % num2)
        
# @lc code=end

