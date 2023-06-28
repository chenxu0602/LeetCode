#
# @lc app=leetcode id=2749 lang=python3
#
# [2749] Minimum Operations to Make the Integer Zero
#

# @lc code=start
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        for k in range(61):
            target = num1 - k * num2
            if target >= 0 and target.bit_count() <= k <= target:
                return k

        return -1
        
# @lc code=end

