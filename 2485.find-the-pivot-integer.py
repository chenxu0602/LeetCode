#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
import math 

class Solution:
    def pivotInteger(self, n: int) -> int:

        # temp = (n * n + n) // 2
        # sq = int(math.sqrt(temp))
        # if sq * sq == temp:
        #     return sq
        # return -1

        x = math.sqrt(n * (n + 1) // 2)
        return -1 if x % 1 else int(x)
        
# @lc code=end

