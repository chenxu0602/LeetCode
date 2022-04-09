#
# @lc app=leetcode id=2180 lang=python3
#
# [2180] Count Integers With Even Digit Sum
#

# @lc code=start
class Solution:
    def countEven(self, num: int) -> int:
        return (num - sum(map(int, str(num))) % 2) // 2
        
# @lc code=end

