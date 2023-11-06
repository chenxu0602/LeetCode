#
# @lc app=leetcode id=2864 lang=python3
#
# [2864] Maximum Odd Binary Number
#

# @lc code=start
from collections import Counter

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        count = Counter(s)
        return '1' * (count['1'] - 1) + '0' * count['0'] + '1'
        
# @lc code=end

