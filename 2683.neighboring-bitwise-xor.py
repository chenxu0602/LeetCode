#
# @lc app=leetcode id=2683 lang=python3
#
# [2683] Neighboring Bitwise XOR
#

# @lc code=start
from functools import reduce
import operator

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        return not reduce(operator.xor, derived)
        
# @lc code=end

