#
# @lc app=leetcode id=3211 lang=python3
#
# [3211] Generate Binary Strings Without Adjacent Zeros
#

# @lc code=start
from itertools import product

class Solution:
    def validStrings(self, n: int) -> List[str]:

        return [''.join(bits) for bits in product('01', repeat=n) if '00' not in ''.join(bits)]
        
# @lc code=end

